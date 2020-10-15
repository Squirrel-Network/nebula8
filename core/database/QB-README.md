# How to use QB (Query Builder)

1. select a table

```python
QB("table")
```

2. perform an operation

```python
QB("table").select()
             .insert()
             .delete()
             .update()
```

3. in case of selecting or inserting select the columns (to select them all use ["*"])

```python
QB("table").select().columns(["a", "b"])
```

4. in case of update select columns and values immediately

```python
QB("table").update().params({"a": 3, "b": "ciao"})
```

5. add any where

```python
QB("table").delete().where("x", "=", 2)
```
