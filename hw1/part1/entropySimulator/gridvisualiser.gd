extends MultiMeshInstance3D

@export var n: int = 10 
@export var total_room_size: float = 20.0

# --- HEATMAP SETTINGS ---
@export var spawner_node: Node3D # We will drag the Spawner here in the Inspector!
@export var max_heat_threshold: int = 5 # 3 particles in a box = 100% red
@export var color_cold: Color = Color(0.0, 0.2, 0.502, 1.0) # Faint blue
@export var color_hot: Color = Color(1.0, 0.0, 0.0, 1.0)  # Bright semi-transparent red

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
		# This ignores any random static nodes sitting in the Spawner by accident!
		if not particle is CharacterBody3D:
			continue
			
		var pos = particle.global_position
		var shift = total_room_size / 2.0
		
		# CRITICAL FIX: floori() returns integers, preventing the Array crash!
		var grid_x = floori((pos.x + shift) / sub_box_size)
		var grid_y = floori((pos.y + shift) / sub_box_size)
		var grid_z = floori((pos.z + shift) / sub_box_size)
		
		if grid_x >= 0 and grid_x < n and grid_y >= 0 and grid_y < n and grid_z >= 0 and grid_z < n:
			var index = grid_x * (n * n) + grid_y * n + grid_z
			grid_counts[index] += 1
			
	for i in range(multimesh.instance_count):
		var count = grid_counts[i]
		var heat = min(float(count) / float(max_heat_threshold), 1.0)
		var new_color = color_cold.lerp(color_hot, heat)
		multimesh.set_instance_color(i, new_color)
