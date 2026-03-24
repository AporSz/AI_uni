extends MultiMeshInstance3D

@export var n: int = 10 
@export var total_room_size: float = 20.0

# --- HEATMAP SETTINGS ---
@export var spawner_node: Node3D 
@export var max_entropy_threshold: float = 0.04 # Changed from 0.53! (0.038 is approx 5 particles out of 1000)
@export var heat_exponent: float = 2.5 # Our exponential curve (Try 1.5 to 3.0)
@export var color_cold: Color = Color(0.0, 0.2, 0.502, 1.0) 
@export var color_hot: Color = Color(1.0, 0.0, 0.0, 1.0)  

var sub_box_size: float
var grid_counts: Array[int] = []

func _ready():
	sub_box_size = total_room_size / float(n)
	
	multimesh = MultiMesh.new()
	multimesh.transform_format = MultiMesh.TRANSFORM_3D
	multimesh.use_colors = true 
	multimesh.instance_count = n * n * n
	
	var box_shape = BoxMesh.new()
	box_shape.size = Vector3.ONE * sub_box_size 
	multimesh.mesh = box_shape
	
	grid_counts.resize(multimesh.instance_count)
	grid_counts.fill(0)
	
	generate_grid()

func generate_grid():
	var index = 0
	var start_pos = -(total_room_size / 2.0) + (sub_box_size / 2.0)
	
	for x in range(n):
		for y in range(n):
			for z in range(n):
				var pos = Vector3(
					start_pos + x * sub_box_size,
					start_pos + y * sub_box_size,
					start_pos + z * sub_box_size
				)
				var transform = Transform3D(Basis(), pos)
				multimesh.set_instance_transform(index, transform)
				multimesh.set_instance_color(index, color_cold)
				index += 1

func _process(_delta):
	if not spawner_node:
		return
		
	grid_counts.fill(0)
	
	for particle in spawner_node.get_children():
		if not particle is CharacterBody3D:
			continue
			
		var pos = particle.global_position
		var shift = total_room_size / 2.0
		
		var grid_x = floori((pos.x + shift) / sub_box_size)
		var grid_y = floori((pos.y + shift) / sub_box_size)
		var grid_z = floori((pos.z + shift) / sub_box_size)
		
		if grid_x >= 0 and grid_x < n and grid_y >= 0 and grid_y < n and grid_z >= 0 and grid_z < n:
			var index = grid_x * (n * n) + grid_y * n + grid_z
			grid_counts[index] += 1
			
	var total_particles = spawner_node.get_child_count()
	
	for i in range(multimesh.instance_count):
		var count = grid_counts[i]
		var entropy = 0.0
		
		if total_particles > 0 and count > 0:
			var p_i = float(count) / float(total_particles)
			entropy = -p_i * (log(p_i) / log(2.0))
		
		# 1. Get the linear fraction using your static threshold
		var linear_heat = min(entropy / max_entropy_threshold, 1.0)
		
		# 2. Apply the exponential curve
		var exponential_heat = pow(linear_heat, heat_exponent)
		
		# 3. Mix the colors
		var new_color = color_cold.lerp(color_hot, exponential_heat)
		
		multimesh.set_instance_color(i, new_color)
