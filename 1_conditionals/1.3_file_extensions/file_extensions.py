def main():
    # get filename as user input 
    filename = input('Filename with extension: ')

    # pring media type
    print(getMediaType(filename.strip()))

def getMediaType(filename):
    # getting the filename extension and matching it to possible values
    match getExtension(filename):
        case '.gif':
            return 'image/gif'
        case '.jpg' | '.jpeg':
            return 'image/jpeg'
        case '.png':
            return 'image/png'
        case '.pdf':
            return 'application/pdf'
        case '.txt':
            return 'text/plain'
        case '.zip':
            return 'application/zip'
        # if no matching case found
        case _: 
            return 'application/octet-stream '


def getExtension(filename):
    # slice the string from the index of the first occurence of "." to the end of the string
    # (getting the extension of the file)
    return filename[filename.find('.'):]

# entry point of the app 
main()