extends Node3D

@export var particle_scene: PackedScene
@export var number_of_particles: int = 100
@export var spawn_area_size: float = 8.0 
@export var current_speed: float = 10.0 # We added this to control the speed!

func _ready():
	spawn_all()

func spawn_all():
	for i in range(number_of_particles):
		spawn_particle()

# The UI will call this function!
func restart_sim(new_count: int, new_speed: float):
	number_of_particles = new_count
	current_speed = new_speed
	
	# Destroy all existing particles
	for child in get_children():
		child.queue_free()
		
	# Spawn the new batch
	spawn_all()

func spawn_particle():
	if not particle_scene: return
		
	var new_particle = particle_scene.instantiate()
	
	# PASS THE SPEED TO THE PARTICLE BEFORE ADDING IT TO THE WORLD
	new_particle.start_speed = current_speed 
	
	var half_size = spawn_area_size / 2.0
	var random_position = Vector3(
		randf_range(-half_size, half_size),
		randf_range(-half_size, half_size), 
		randf_range(-half_size, half_size)
	)
	
	new_particle.position = random_position
	add_child(new_particle)
