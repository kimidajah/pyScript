class Hero:
    def __init__(self, name, damage, meta, role):
        self.name = name
        self.damage = damage
        self.meta = meta
        self.role = role

    def get_name(self):
        return f"ini adalah hero {self.name}, "
    
    def get_damage(self):
        return f"damage {self.name} adalah {self.damage}"
    
    def get_meta(self):
        if(self.meta):
            return f"saya sangat meta di versiion sekatang"
        else:
            return f"saya tidak meta di version sekarang"
    
    def get_role(self):
        return f"role saya {self.role}"
    
    def get_all_data (self) :
        return f"{self.get_name()} {self.get_damage()} {self.get_meta()} {self.get_role()}"
