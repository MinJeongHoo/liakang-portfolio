from django.core.management.base import BaseCommand
from works.models import WorkMaterial
from works.models import WorksModel
from works.models import WorkSize
from django.contrib.admin.utils import flatten
from workcategory.models import WorksCategoryModel
import cloudinary
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many material do you want to create")

    def handle(self, *args, **options):
        arr = [
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/1.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/2.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/3.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/4.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/5.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/6.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/7.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/8.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/9.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/10.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/11.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/12.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/13.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/14.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/15.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/16.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/17.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/18.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/19.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/20.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/21.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/22.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/23.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/24.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/25.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/26.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/27.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/28.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/29.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/30.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/31.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/32.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/33.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/34.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/35.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/36.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/37.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/38.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/39.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/40.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/41.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/42.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/43.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/44.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/45.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/46.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/47.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/48.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/49.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/50.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/51.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/52.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/53.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/54.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/55.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/56.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/57.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/58.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/59.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/60.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/61.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/62.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/63.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/64.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/65.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/66.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/67.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/68.jpg"],
            ["7", "Drawing", "", "", "", MEDIA_ROOT+"/drawing/69.jpg"]
        ]

        for item in arr:
            category = WorksCategoryModel.objects.get(pk=item[0])
            WorksModel.objects.create(
                category=category, worksTitle=item[1], image=cloudinary.uploader.upload(item[5]))
        self.stdout.write(self.style.SUCCESS("Works created!"))
