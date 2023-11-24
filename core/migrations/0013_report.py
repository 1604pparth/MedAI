# Generated by Django 4.1.5 on 2023-11-06 18:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_doctorprofile_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('disease', models.CharField(max_length=60)),
                ('HighBP', models.IntegerField(default=0)),
                ('HighChol', models.IntegerField(default=0)),
                ('BMI', models.IntegerField(default=0)),
                ('Stroke', models.IntegerField(default=0)),
                ('HeartDiseaseAttack', models.IntegerField(default=0)),
                ('GenHlth', models.IntegerField(default=0)),
                ('Age', models.IntegerField(default=0)),
                ('DoctorConclusion', models.IntegerField(default=1)),
                ('DoctorPrescription', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctorprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patientprofile')),
            ],
        ),
    ]