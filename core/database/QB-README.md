# Come usare QB

1. selezionare una tabella

```python
QB("tabella")
```

2. eseguire un operazione

```python
QB("tabella").select()
             .insert()
             .delete()
             .update()
```

3. in caso di select o insert selezionare le colonne (per selezionarle tutte usare ["*"])

```python
QB("tabella").select().columns(["a", "b"])
```

4. in caso di update selezionare colonne e valori subito

```python
QB("tabella").update().params({"a": 3, "b": "ciao"})
```

5. aggiungere una eventuale where

```python
QB("tabella").delete().where("x", "=", 2)
```