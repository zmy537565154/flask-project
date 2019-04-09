from app.base import BaseResource



class FirstApi(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser.add_argument('name', required=True, type=str,
                                 location=['form', 'json', 'args', 'files', 'values', 'headers'])

    def get(self):
        return 'POST request only'

    def post(self):
        params = self.parser.parse_args()
        name = params['name']
        result = name+',hello!'
        return result
