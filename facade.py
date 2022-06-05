class ResourceManager:
    def __init__(self):
        print("Update all resources.")


    def update_resources(self):
        self.reportDb = ReportDb()
        self.reportDb.update()

        self.systemDb = SystemDb()
        self.systemDb.save()

        self.site = Site()
        self.site.update()

        self.Api = Api()
        self.Api.post()

class ReportDb:
    def __init__(self):
        print ("ReportDb called.")

    def update(self):
        print("ReportDb updated.")

class SystemDb:
    def __init__(self):
        print("SystemDb called.")

    def save(self):
        print("SystemDb updated.")

class Site:
    def __init__(self):
        print("SiteDb called.")

    def update(self):
        print("Site updated.")

class Api:
    def __init__(self):
        print("Api called.")

    def post(self):
        print("Api post called.")

resource_manager =  ResourceManager()
resource_manager.update_resources()