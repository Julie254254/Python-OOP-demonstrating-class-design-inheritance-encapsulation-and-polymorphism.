# Activity 1: Design Your Own Class 🏗️

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Derived class (inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)
        self.storage = storage
        self.camera = camera
    
    def take_photo(self):
        return f"📸 Taking a photo with {self.camera} camera!"
    
    def install_app(self, app_name):
        return f"📱 Installing {app_name} on {self.model}..."
    
    # Encapsulation example: private attribute
    __os_version = "1.0"
    
    def update_os(self, new_version):
        self.__os_version = new_version
        return f"🔄 {self.model} updated to OS version {self.__os_version}"

# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 14", "128GB", "12MP")
    phone2 = Smartphone("Samsung", "Galaxy S23", "256GB", "50MP")

    print(phone1.info())
    print(phone1.take_photo())
    print(phone2.install_app("WhatsApp"))
    print(phone1.update_os("2.0"))
