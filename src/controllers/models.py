from flask_restx import fields

stock = {"id" : fields.Integer, "code": fields.String, "name":fields.String, "market":fields.String}
quote = {"DateTime" : fields.DateTime("iso8601"), "Open": fields.Float, "High":fields.Float, "Low":fields.Float, "Close":fields.Float, "Volume":fields.Float}
fieldError = {"field" : fields.String, "error": fields.String}