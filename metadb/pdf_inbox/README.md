# PDF inbox

Drop manually-downloaded PDFs here for paywalled-venue papers (TII / ESWA, etc.)
that `--deep` could not auto-fetch.

**Filename convention**: name each file `<short-id>.pdf` (or `P-<short-id>.pdf`)
using the `short_id` from the report's `manifest.json`.

Example:
```
metadb/pdf_inbox/IEEETRAN-bf3127.pdf
metadb/pdf_inbox/EXPERTSY-537c52.pdf
```

Then run from repo root:
```
python -m skills.topic_finder.scripts.import_pdf \
    --manifest reports/<stem>/manifest.json --inbox
```

Successfully imported files move to `metadb/pdf_inbox/.imported/` so this
folder stays clean for the next batch.

## Alternative: drop directly into the report folder

You may also drop PDFs into the report bundle next to `manifest.json`
(naming convention `P-<short-id>.pdf`, matching how arXiv PDFs already sit
there). Then point `--inbox-dir` at that folder:

```
cp ~/Downloads/coma.pdf reports/<stem>/P-IEEETRAN-bf3127.pdf

python -m skills.topic_finder.scripts.import_pdf \
    --manifest reports/<stem>/manifest.json \
    --inbox --inbox-dir reports/<stem>/
```

Files dropped into the report folder are **kept in place** after import
(they belong with the rest of the bundle). Already-cached papers are
skipped silently so re-running is safe.

## Single-file mode

When you only have one PDF and don't want to rename it:

```
python -m skills.topic_finder.scripts.import_pdf \
    --pdf ~/Downloads/whatever.pdf \
    --manifest reports/<stem>/manifest.json \
    --short-id IEEETRAN-bf3127
```
