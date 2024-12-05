from rest_framework import serializers

from core.apps.content.models.break_items import Break
from core.apps.content.models.content import Content


class ContentListSerializer(serializers.ModelSerializer):

    # contentlar sonini olish (qisimlarini)
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        count = obj.contents.count()
        ova = obj.ova.count()

        chronology = obj.ova.count()
        return {"count": count, "ova": ova, "chronology": chronology}

    class Meta:
        model = Content
        fields = (
            "id",
            "poster_desktop",
            "poster_mobile",
            "poster_video",
            "poster_card",
            "title",
            "genre",
            "category",
            "age_limit",
            "release_date",
            "count",
        )
        depth = 2


class ContentRetriveSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        count = obj.contents.count()
        ova = obj.ova.count()
        chronology = obj.ova.count()
        return {"count": count, "ova": ova, "chronology": chronology}

    # fasillarni olish
    breaks = serializers.SerializerMethodField()

    def get_breaks(self, obj):
        # Retrieve the associated breaks for the Content instance
        try:
            breaks_items = Break.objects.get(item__break_item=obj)
        except:
            return []
        breaks = []
        for i in breaks_items.item.all():
            breaks.append({"id": i.break_item.id, "title": i.break_item.title, "poster": i.break_item.poster_desktop})

        return breaks

    class Meta:
        model = Content
        fields = "__all__"
        depth = 2
