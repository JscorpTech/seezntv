from django.core import management
from core.apps.content import models
from core.apps.api import models as mm


class Command(management.BaseCommand):
    base_urls = ["https://f005.backblazeb2.com/file/seezntv", "https://seezntv.s3.us-east-005.backblazeb2.com"]

    def __remove_domain(self, data: str) -> str:
        for url in self.base_urls:
            data = data.replace(url, "")
        return data

    def __make_url(self, folder, url):
        return "%s%s" % (folder, self.__remove_domain(url))

    def import_cadr(self):
        cadrs = models.Cadr.objects.all()
        for i in cadrs:
            print(mm.CadrModel.objects.create(image=self.__make_url("/cadr", i.cadr)))

    def import_istory(self):
        istories = models.Istory.objects.all()
        for i in istories:
            itory = mm.IstoryModel.objects.create(content_uz=i.content)
            for video in i.videos.all():
                video = mm.IstoryVideoModel.objects.create(video=self.__make_url("/video", video.video))
                itory.videos.add(video)

    def import_content(self):
        contents = models.Content.objects.all()
        for i in contents:
            content = mm.ContentModel.objects.create(
                title_uz=i.title,
                description_uz=i.description,
                poster_desktop=self.__make_url("poster", i.poster_desktop),
                poster_mobile=self.__make_url("poster", i.poster_mobile),
                poster_card=self.__make_url("poster", i.poster_card),
                poster_video=self.__make_url("poster", i.poster_video),
                age_limit=i.age_limit,
                release_date=i.release_date,
            )
            for genre in i.genre.all():
                content.genre.add(mm.GenreModel.objects.get_or_create(name_uz=genre.genre.item)[0])
            for cadr in i.kadrs.all():
                content.cadrs.add(mm.CadrModel.objects.get_or_create(image=self.__make_url("/cadr", cadr.cadr))[0])
            for category in i.category.all():
                content.category.add(mm.CategoryModel.objects.get_or_create(name_uz=category.category.item)[0])
            for cc in i.contents.all():
                media = mm.MediaModel.objects.get_or_create(
                    video=self.__make_url("/video", cc.sources),
                    skip_start_time=cc.skip_start_time,
                    skip_end_time=cc.skip_end_time,
                    position=cc.index,
                )[0]
                content.contents.add(media)
            for cc in i.chronology.all():
                media = mm.MediaModel.objects.get_or_create(
                    video=self.__make_url("/video", cc.sources),
                    skip_start_time=cc.skip_start_time,
                    skip_end_time=cc.skip_end_time,
                    position=cc.index,
                )[0]
                content.chronology.add(media)

            for cc in i.ova.all():
                media = mm.MediaModel.objects.get_or_create(
                    video=self.__make_url("/video", cc.sources),
                    skip_start_time=cc.skip_start_time,
                    skip_end_time=cc.skip_end_time,
                    position=cc.index,
                )[0]
                content.ova.add(media)

    def import_video(self):
        content = mm.ContentModel.objects.all()
        for i in content:
            for media in i.contents.all():
                mm.VideoModel.objects.create(
                    video=media.video,
                    name=media.name,
                    content=i,
                    skip_start_time=media.skip_start_time,
                    skip_end_time=media.skip_end_time,
                    position=media.position,
                )

    def import_cadrs(self):
        content = mm.ContentModel.objects.all()
        for i in content:
            for cadr in i.cadrs.all():
                cadr.content = i
                cadr.save()

    def handle(self, *args, **options) -> str | None:
        # self.import_cadrs()
        # self.import_content()
        # self.import_istory()
        # self.import_cadr()
        contents = mm.ContentModel.objects.all()
        from urllib.parse import unquote
        for i in contents:
            i.poster_desktop.name = unquote(i.poster_desktop.name)
	        i.save()
