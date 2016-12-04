from .. import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(30), unique=True, nullable=False)
    description = db.Column(db.Unicode(500))

    def __repr__(self):
        return "<Category %r>" % self.name

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('packages', lazy='dynamic'))

    @property
    def full_name(self):
        return "%s/%s" % (self.category.name, self.name)

    def __repr__(self):
        return "<Package '%s/%s'>" % (self.category.name, self.name)

class PackageVersion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Unicode(128), nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)
    package = db.relationship('Package', backref=db.backref('versions', lazy='dynamic'))

    def __repr__(self):
        return "<PackageVersion '%s/%s-%s'>" % (self.package.category.name, self.package.name, self.version)
