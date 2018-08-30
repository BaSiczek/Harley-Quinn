import math, pyglet
from pyglet.window import key
from game import physicalobject, resources, bullet

class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image,
                                    *args, **kwargs)

        self.key_handler = key.KeyStateHandler()
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.bullet_speed = 500.0
        self.reacts_to_bullets = False

    def delete(self):
        super(Player, self).delete()



    def fire(self):
        angle_radians = -math.radians(self.rotation)
        ship_radius = self.image.width/2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        bullet_vx = (
            self.velocity_x +
            math.cos(angle_radians) * self.bullet_speed
            )
        bullet_vy = (
            self.velocity_y +
            math.sin(angle_radians) * self.bullet_speed
            )
        new_bullet.velocity_x = -bullet_vx
        new_bullet.velocity_y = -bullet_vy
        self.new_objects.append(new_bullet)



    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x -= force_x
            self.velocity_y -= force_y
        if self.key_handler[key.SPACE]:
            self.fire()
