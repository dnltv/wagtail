# Generated by Django 3.0.4 on 2020-04-06 09:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.test.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0048_importantpages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="streampage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.CharBlock()),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.test.testapp.models.ExtendedImageChooserBlock()),
                    (
                        "product",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("price", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    ("raw_html", wagtail.blocks.RawHTMLBlock()),
                ]
            ),
        ),
    ]