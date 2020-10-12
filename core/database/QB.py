import copy


class QB():
    def __init__(self, table):
        self.table = table
        self.query = ""
        self.operator = ""
        self.columns_list = ""
        self.optClause = ""
        self.distinctClause = ""

    def distinct(self):
        self.distinctClause = "DISTINCT"

        return self

    def select(self):
        self.operator = "select"
        self.query = f"SELECT <distinct> <cols> FROM {self.table}"

        return self

    def delete(self):
        self.operator = "delete"
        self.query = f"DELETE FROM {self.table}"

        return self

    def insert(self):
        self.operator = "insert"
        self.query = f"INSERT INTO {self.table} <cols> VALUES (<values>)"

        return self

    def update(self):
        self.operator = "update"
        self.query = f"UPDATE {self.table} SET <cols-values>"

        return self

    def params(self, colsvalues):
        colsValues = []

        for col, val in colsvalues.items():
            colsValues.append(f"{col} = {val}")

        self.query = self.query.replace("<cols-values>", ", ".join(colsValues))

        return self

    def columns(self, columns):
        if columns[0] == "*":
            if self.operator == "select":
                columns_list = "*"
            else:
                columns_list = ""
        else:
            if self.operator == "select":
                columns_list = ", ".join(columns)
            else:
                columns_list = "(" + ", ".join(columns) + ")"

        self.query = self.query.replace("<cols>", columns_list)

        return self

    def values(self, values):
        values_list = ", ".join([str(v) for v in values])
        self.query = self.query.replace("<values>", values_list)

        return self

    def where(self, column, relation, value=None):
        self.optClause += f" WHERE {column} {relation}"

        if not (relation in ("IS NOT NULL", "IS NULL")):
            if value is None:
                raise ValueError("manca il valore per la relazione")

            value = str(value)
            self.optClause += f" {value}"

        return self

    def whereAnd(self, column, relation, value=None):
        self.optClause += f" AND {column} {relation}"

        if not (relation in ("IS NOT NULL", "IS NULL")):
            if value is None:
                raise ValueError("manca il valore per la relazione")
            self.optClause += f" {value}"

        return self

    def whereOr(self, column, relation, value=None):
        self.optClause += f" OR {column} {relation}"

        if not (relation in ("IS NOT NULL", "IS NULL")):
            if value is None:
                raise ValueError("manca il valore per la relazione")
            self.optClause += f" {value}"

        return self

    def orderBy(self, columns):
        orderList = []

        for col, order in columns.items():
            orderList.append(f"{col} {order}")

        orderString = ", ".join(orderList)
        self.optClause += f" ORDER BY {orderString}"

        return self

    def limit(self, limit, offset=0):
        self.optClause += f" LIMIT {limit}"

        if offset > 0:
            self.optClause += f" OFFSET {offset}"

        return self

    def groupBy(self, columns):
        columns_list = ", ".join(columns)
        self.optClause += f" GROUP BY {columns_list}"

        return self

    def buildQuery(self):
        self.query = self.query.replace("<distinct>", self.distinctClause)
        finalQuery = self.query + self.optClause

        return finalQuery.replace("  ", " ")
