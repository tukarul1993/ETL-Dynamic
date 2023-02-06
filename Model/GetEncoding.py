
class GetEncoding:
    def get_encoding(self,file):
        print("inside get encoding")
        with open(file, 'rb') as f:
            contents = f.read()
            try:
                contents.decode('utf-8')
                return 'utf-8'
            except:
                pass
            try:
                contents.decode('utf-16')
                return 'utf-16'
            except:
                pass
            try:
                contents.decode('utf-32')
                return 'utf-32'
            except:
                pass
            return 'unknown'
