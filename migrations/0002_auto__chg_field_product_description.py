# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Product.description'
        db.alter_column('SOS_product', 'description', self.gf('django.db.models.fields.TextField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Product.description'
        db.alter_column('SOS_product', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
        'SOS.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        }
    }

    complete_apps = ['SOS']
