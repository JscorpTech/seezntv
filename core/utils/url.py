from urllib.parse import unquote


class Url:

    @staticmethod
    def unquote_if_exists(data, fields) -> str:
        for field in fields:
            if field in data:
                data[field] = unquote(data[field])
        return data
