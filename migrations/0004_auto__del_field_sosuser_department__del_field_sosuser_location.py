# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'SOSuser.department'
        db.delete_column('SOS_sosuser', 'department_id')

        # Deleting field 'SOSuser.location'
        db.delete_column('SOS_sosuser', 'location_id')

        # Adding M2M table for field department on 'SOSuser'
        db.create_table('SOS_sosuser_department', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sosuser', models.ForeignKey(orm['SOS.sosuser'], null=False)),
            ('department', models.ForeignKey(orm['SOS.department'], null=False))
        ))
        db.create_unique('SOS_sosuser_department', ['sosuser_id', 'department_id'])

        # Adding M2M table for field location on 'SOSuser'
        db.create_table('SOS_sosuser_location', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sosuser', models.ForeignKey(orm['SOS.sosuser'], null=False)),
            ('location', models.ForeignKey(orm['SOS.location'], null=False))
        ))
        db.create_unique('SOS_sosuser_location', ['sosuser_id', 'location_id'])


    def backwards(self, orm):
        
        # Adding field 'SOSuser.department'
        db.add_column('SOS_sosuser', 'department', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['SOS.Department']), keep_default=False)

        # Adding field 'SOSuser.location'
        db.add_column('SOS_sosuser', 'location', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['SOS.Location']), keep_default=False)

        # Removing M2M table for field department on 'SOSuser'
        db.delete_table('SOS_sosuser_department')

        # Removing M2M table for field location on 'SOSuser'
        db.delete_table('SOS_sosuser_location')


    models = {
        'SOS.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'SOS.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'SOS.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'SOS.sosuser': {
            'Meta': {'object_name': 'SOSuser', '_ormbases': ['auth.User']},
            'department': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['SOS.Department']", 'symmetrical': 'False'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['SOS.Location']", 'symmetrical': 'False'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['SOS']
