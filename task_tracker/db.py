import tinydb


class DB:
    def __init__(self, db_path, db_file_prefix, table_name):
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json", create_dirs=True
        )
        self._table_name = table_name 
        
    def create(self, item: dict) -> int:
        id = self.get_table().insert(item)
        return id

    def update(self, id: int, mods) -> None:
        changes = {k: v for k, v in mods.items() if v is not None}
        self.get_table().update(changes, doc_ids=[id])
    
    def delete(self, id):
        self.get_table().remove(doc_ids=[id])
    
    def get(self, id: int):
        return self.get_table().get(doc_id=id)
    
    def list(self):
        return self.get_table().all()
    
    def clear(self):
        self.get_table().truncate()
    
    def close(self):
        self._db.close()
        
    def get_table(self):
        return self._db.table(self._table_name)