class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
