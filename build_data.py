
# build_data.py
# Lee tu CSV "series_numeradas.csv" (mismo directorio), y genera "data_hashed.json"
# que NO contiene los títulos en texto plano. El HTML usa ese JSON para validar.
import csv, json, secrets, hashlib, re, unicodedata, sys, os

CSV_NAME = "series_numeradas.csv"
OUT_JSON = "data_hashed.json"

def normalize_py(s: str) -> str:
    # Mantiene acentos, ignora mayúsculas/minúsculas, quita puntuación/símbolos, colapsa espacios
    s = str(s)
    s = unicodedata.normalize("NFC", s).lower().strip()
    s = re.sub(r"\s+", " ", s, flags=re.UNICODE)
    out_chars = []
    for ch in s:
        cat = unicodedata.category(ch)
        if cat.startswith("L") or cat == "Nd" or ch == " ":
            out_chars.append(ch)
    return "".join(out_chars)

def read_rows(path):
    # Detecta columnas típicas
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        headers = [h.strip() for h in r.fieldnames or []]
        # posibles nombres
        num_keys = {"num","número","numero","id","indice","índice"}
        title_keys = {"titulo","título","title","nombre","serie","nombre_serie"}
        num_col = next((h for h in headers if h.lower() in num_keys), None)
        title_col = next((h for h in headers if h.lower() in title_keys), None)
        rows = list(r)
    if num_col is None or title_col is None:
        # fallback: asumir 1ª y 2ª columna
        with open(path, "r", encoding="utf-8-sig", newline="") as f2:
            r2 = csv.reader(f2)
            headers = next(r2)
            data = list(r2)
            out = []
            for row in data:
                if not row: continue
                num = int(row[0])
                title = row[1] if len(row) > 1 else ""
                out.append((num, title))
            return out
    out = []
    for row in rows:
        num = int(row[num_col])
        title = str(row[title_col])
        out.append((num, title))
    return out

def main():
    if not os.path.exists(CSV_NAME):
        print(f"ERROR: No encuentro {CSV_NAME}. Ponlo en esta misma carpeta.", file=sys.stderr)
        sys.exit(1)
    pairs = read_rows(CSV_NAME)
    items = []
    for num, title in pairs:
        salt = secrets.token_hex(8)
        digest = hashlib.sha256((salt + normalize_py(title)).encode("utf-8")).hexdigest()
        items.append({"num": int(num), "audio": f"{int(num)}.wav", "salt": salt, "hash": digest})
    items.sort(key=lambda x: x["num"])
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, ensure_ascii=False, indent=2)
    print(f"Listo: {OUT_JSON} creado con {len(items)} elementos.")

if __name__ == "__main__":
    main()
