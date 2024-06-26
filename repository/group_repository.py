from model.group import Group
from data.db_provider import DbProvider
from mapping.group_mapping import group_from_row


class GroupRepository:
    
    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider
    
    def read_all(self) -> list[Group]:
        rows = self.db_provider.execute_read_query('''SELECT * from groups''')
        return list(map(group_from_row, rows))
    
    def read_by_id(self, id: int) -> Group:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM groups WHERE id = %s''',
            (id,)
        )        
        return group_from_row(rows[0])
