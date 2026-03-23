extends CharacterBody3D

@export var start_speed: float = 10.0

func _ready():
	# Give the particle a random starting direction
	# (You can change this to a specific vector if you prefer)
	var random_dir = Vector3(
		randf_range(-1.0, 1.0), 
		randf_range(-1.0, 1.0), 
		randf_range(-1.0, 1.0)
	).normalized()
	
	velocity = random_dir * start_speed

func _physics_process(delta: float):
	# 1. Move the particle and check for collisions
	# move_and_collide returns a KinematicCollision3D object if it hits something
	var collision = move_and_collide(velocity * delta)
	
	if collision:
		# 2. Get the normal (the perpendicular angle) of the wall we hit
		var wall_normal = collision.get_normal()
		
		# 3. Reflect our velocity perfectly off that wall
		velocity = velocity.bounce(wall_normal)
		
		# 4. PREVENT ENERGY LOSS: Calculate the remaining distance for this frame
		var remainder = collision.get_remainder()
		
		# Bounce that remaining distance as well, and move the particle the rest of the way
		remainder = remainder.bounce(wall_normal)
		move_and_collide(remainder)
