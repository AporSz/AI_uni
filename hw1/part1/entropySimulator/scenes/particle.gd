extends CharacterBody3D

@export var start_speed: float = 10.0
@export var mass: float = 1.0 

func _ready():
	# Give the particle a random starting direction
	var random_dir = Vector3(
		randf_range(-1.0, 1.0), 
		randf_range(-1.0, 1.0), 
		randf_range(-1.0, 1.0)
	).normalized()
	velocity = random_dir * start_speed

func _physics_process(delta: float):
	var collision = move_and_collide(velocity * delta)
	
	if collision:
		var collider = collision.get_collider()
		var normal = collision.get_normal()
		var remainder = collision.get_remainder()
		
		# ==========================================
		# SCENARIO 1: We hit a Wall
		# ==========================================
		if collider is StaticBody3D:
			velocity = velocity.bounce(normal)
			remainder = remainder.bounce(normal)
			move_and_collide(remainder)
			
		# ==========================================
		# SCENARIO 2: We hit another Particle
		# ==========================================
		elif collider is CharacterBody3D:
			var x1 = global_position
			var x2 = collider.global_position
			var v1 = velocity
			var v2 = collider.velocity
			
			var pos_diff = x1 - x2
			var vel_diff = v1 - v2
			
			# CRITICAL SEPARATION CHECK:
			# If the dot product is positive, the particles are already moving apart.
			# This prevents the engine from double-calculating the collision if both 
			# particles detect each other in the exact same frame!
			if vel_diff.dot(pos_diff) >= 0:
				return
				
			var dist_sq = pos_diff.length_squared()
			if dist_sq < 0.0001: 
				return # Safety check to prevent division by zero
				
			var m1 = mass
			var m2 = collider.mass
			
			# Calculate new velocity for THIS particle
			var mass_ratio_1 = (2.0 * m2) / (m1 + m2)
			var dot_prod = vel_diff.dot(pos_diff)
			var velocity_change_1 = (mass_ratio_1 * dot_prod / dist_sq) * pos_diff
			
			# Calculate new velocity for the OTHER particle
			var mass_ratio_2 = (2.0 * m1) / (m1 + m2)
			var velocity_change_2 = (mass_ratio_2 * (-vel_diff).dot(-pos_diff) / dist_sq) * (-pos_diff)
			
			# Apply the new perfectly elastic velocities to BOTH particles instantly
			velocity = v1 - velocity_change_1
			collider.velocity = v2 - velocity_change_2
			
			# Bounce the remaining distance so they don't end the frame stuck together
			remainder = remainder.bounce(normal)
			move_and_collide(remainder)
