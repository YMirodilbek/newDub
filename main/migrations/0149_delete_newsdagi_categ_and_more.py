# Generated by Django 5.1.2 on 2024-11-12 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0148_remove_room_luxury_kv1_remove_room_luxury_price1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsdagi_Categ',
        ),
        migrations.DeleteModel(
            name='Newsdagi_malumot_ongtomondagi',
        ),
        migrations.DeleteModel(
            name='Newsdagi_rasm',
        ),
        migrations.DeleteModel(
            name='Newsdagi_rasmdi_tagdagi_sozlar',
        ),
        migrations.DeleteModel(
            name='NewsdagiDeta',
        ),
        migrations.DeleteModel(
            name='Newsdi_button',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title1_en',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title1_ja',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title2_en',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title2_ja',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title3_en',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title3_ja',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title4_en',
        ),
        migrations.RemoveField(
            model_name='header_news',
            name='title4_ja',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title1_en',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title1_ja',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title2_en',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title2_ja',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title3_en',
        ),
        migrations.RemoveField(
            model_name='news_butondi_tepasdagi_matn',
            name='title3_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text1_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text1_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text2_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text2_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text3_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='text3_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title1_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title1_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title2_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title2_ja',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title3_en',
        ),
        migrations.RemoveField(
            model_name='words_news',
            name='title3_ja',
        ),
    ]
