from django.db import models
from django.contrib.auth.models import User


def image_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_audios/%Y/%m/%d/', filename)

def image_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.anonymous_tip.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.anonymous_tip.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.anonymous_tip.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.anonymous_tip.id, 'evidence_audios/%Y/%m/%d/', filename)


designation_choice = (
    ('DGP', 'Director General of Police'),
    ('ADGP', 'Addl. Director General of Police'),
    ('IGP', 'Inspector General of Police'),
    ('DIGP', 'Deputy Inspector General of Police'),
    ('SPDCP', 'Superintendent of police Deputy Commissioner of Police(Selection Grade)'),
    ('SPDCPJ', 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)'),
    ('ASPADCP', 'Addl. Superintendent of police Addl.Deputy Commissioner of Police'),
    ('ASP', 'Assistant Superintendent of Police'),
    ('INSP', 'Inspector of Police'),
    ('SUB_INSP', 'Sub Inspector of Police.'),
    ('HVLDRM', 'Asst. Sub. Inspector/Havildar Major'),
    ('HVLDR', 'Havildar.'),
    ('LN', 'Lance Naik.'),
    ('CONS', 'Constable.'),
)


class Police(User):
    police_id = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, choices=designation_choice, null=True)
    ward= models.ForeignKey('Ward',on_delete=models.PROTECT,null=False)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Police'

    def __str__(self):
        return self.username


ward_choice = (
('HYD01w1','Kapra'),
('HYD01w2','Uppal'),
('HYD01w3','Hayathnagar'),
('HYD01w4','L.B Nagar'),
('HYD01w5','Saroornagar'),
('HYD02w6','Malakpet'),
('HYD02w7','Santhosh Nagar'),
('HYD02w8','Chandrayangutta'),
('HYD02w9','Charminar'),
('HYD02w10','Falaknuma'),
('HYD02w11','Rajendra nagar'),
('HYD03w12','Mehdipatnam'),
('HYD03w13','Karwan'),
('HYD03w14','Goshamahal'),
('HYD03w15','Khairathabad'),
('HYD03w16','Jubilee Hills'),
('HYD04w17','Amberpet'),
('HYD04w18','Musheerabad'),
('HYD04w19','Malkajgiri'),
('HYD04w20','Secunderabad'),
('HYD04w21','Begumpet'),
('HYD05w22','Yusufguda'),
('HYD05w23','Serilingampelli'),
('HYD05w24','Chandannagar'),
('HYD05w25','Patancheru'),


)




class Ward(models.Model):
    id = models.CharField(max_length=255, primary_key=True, choices=ward_choice)  # eg: RJ01w1,RJ01w2,RJ15w5
    address = models.CharField(max_length=255, blank=False)

    def get_contacts(self):
        contact_list = [i.contact for i in Ward.objects.get(id=self.id).contact_set]
        return contact_list

    def __str__(self):
        return self.id


class Contact(models.Model):
    ward = models.ForeignKey('ward',on_delete=models.PROTECT)
    contact = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.ward






class Criminal(models.Model):
    name = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    caste = models.CharField(max_length=255)
    ward=models.ForeignKey(Ward,null=True,on_delete=models.PROTECT)
    birth_mark_desc=models.TextField()
    height=models.CharField(max_length=255)
    complexion=models.CharField(max_length=255)
    eyes=models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics',null=True)

    def __str__(self):
        return self.name

class Missing(models.Model):
    name = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    Area = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    birth_mark_desc=models.TextField()
    height=models.CharField(max_length=255)
    complexion=models.CharField(max_length=255)
    eyes=models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics',null=True)

    def __str__(self):
        return self.name
