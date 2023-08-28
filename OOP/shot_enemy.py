class Person(object):
    def __init__(self, name):
        self.name = name
        self.gun = None
        self.hp = 100

    def install_bullet_into_clip(self, bullet, clip):
        print("%s往弹夹内装了一枚子弹" % self.name)
        clip.install_bullet(bullet)

    def get_gun(self, gun):
        print("%s拿起了%s枪" % (self.name, gun.name))
        self.gun = gun

    def install_clip_into_gun(self, clip, gun):
        print("%s将弹夹装入了%s枪" % (self.name, gun.name))
        gun.install_clip(clip)

    def shot(self, target):
        print("%s对%s开了一枪" % (self.name, target.name))
        self.gun.attack(target)

    def lose_hp(self, bullet):
        self.hp -= bullet.power
        if self.hp <= 0:
            self.die()
        else:
            print("%s还剩%s滴血" % (self.name, self.hp))

    def die(self):
        print("%s死了" % self.name)


class Gun(object):
    def __init__(self, name):
        self.name = name
        self.clip = None

    def install_clip(self, clip):
        self.clip = clip

    def attack(self, target):
        bullet = self.clip.bullets.pop()
        target.lose_hp(bullet)


class Clip(object):
    def __init__(self):
        self.bullets = list()

    def __str__(self):
        return "弹夹内有%d颗子弹" % len(self.bullets)

    def install_bullet(self, bullet):
        self.bullets.append(bullet)


class Bullet(object):
    def __init__(self, power):
        self.power = power


if __name__ == "__main__":
    laowang = Person("老王")
    enemy = Person("敌人")
    clip = Clip()
    bullet_1 = Bullet(50)
    bullet_2 = Bullet(60)
    ak47 = Gun("AK47")
    laowang.install_bullet_into_clip(bullet_1, clip)
    laowang.install_bullet_into_clip(bullet_2, clip)
    laowang.get_gun(ak47)
    laowang.install_clip_into_gun(clip, ak47)
    laowang.shot(enemy)
    laowang.shot(enemy)
    print("DONE")
