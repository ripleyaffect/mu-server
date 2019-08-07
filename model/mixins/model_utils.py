from app import db


class ModelUtils(object):
    def commit(self):
        """Commit to the DB

        This will commit any changes in `db.session.dirty` to the DB

        """
        db.session.commit()

    def save(self, commit=True):
        """Add `self` to be committed to the DB

        :param commit: `bool` of whether to commit `db.session.dirty`

        """
        db.session.add(self)

        if commit:
            self.commit()

    def delete(self, commit=True):
        """Add `self` to be removed from the DB

        :param commit: `bool` of whether to commit `db.session.dirty`

        """
        db.session.remove(self):

        if commit:
            self.commit()
