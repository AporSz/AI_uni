extends Node3D

@export var particle_scene: PackedScene
@export var number_of_particles: int = 1000
# Since your box is 10x10x10, an 8x8x8 spawn area keeps them safely away from the walls initially
@export var spawn_area_size: float = 8.0 

func _ready():
	# This loop runs exactly 'number_of_particles' times right when the game starts
	for i in range(number_of_particles):
		spawn_particle()

func spawn_particle():
	# Safety check in case you forget to assign the scene in the Inspector
	if not particle_scene:
		push_error("Particle Scene is missing! Please assign it in the Inspector.")
		return
		
	# 1. Create a new copy of the particle scene
	var new_particle = particle_scene.instantiate()
	
	# 2. Calculate a random position within our safe spawn area
	var half_size = spawn_area_size / 2.0
	var random_position = Vector3(
		randf_range(-half_size, half_size),
		randf_range(-half_size, half_size), # Assumes your box is centered at Y = 0
		randf_range(-half_size, half_size)
	)
	
	# 3. Move the particle to that random position
	new_particle.position = random_position
	
	# 4. Add it to the world
	add_child(new_particle)
