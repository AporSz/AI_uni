extends Camera3D

@export var move_speed: float = 10.0
@export var mouse_sensitivity: float = 0.002

# We store the rotation to prevent the camera from flipping upside down
var pitch: float = 0.0
var yaw: float = 0.0

func _ready():
	# Hides the mouse cursor and locks it to the center of the game window
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	
	# Grab the initial rotation so the camera doesn't snap on the first frame
	pitch = rotation.x
	yaw = rotation.y

func _unhandled_input(event):
	# Handle mouse movement for looking around
	if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		yaw -= event.relative.x * mouse_sensitivity
		pitch -= event.relative.y * mouse_sensitivity
		
		# Clamp the pitch so you can't look further than straight up or straight down
		pitch = clamp(pitch, -PI/2, PI/2)
		
		rotation.x = pitch
		rotation.y = yaw

	# Press 'Escape' to free the mouse cursor so you can close the game
	if event is InputEventKey and event.pressed and event.keycode == KEY_ESCAPE:
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		
	# Click the mouse on the screen to recapture it
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _process(delta):
	# Only allow movement if the mouse is currently captured
	if Input.get_mouse_mode() != Input.MOUSE_MODE_CAPTURED:
		return
		
	var direction = Vector3.ZERO
	
	# Check standard WASD keys for horizontal movement
	if Input.is_physical_key_pressed(KEY_W):
		direction -= transform.basis.z
	if Input.is_physical_key_pressed(KEY_S):
		direction += transform.basis.z
	if Input.is_physical_key_pressed(KEY_A):
		direction -= transform.basis.x
	if Input.is_physical_key_pressed(KEY_D):
		direction += transform.basis.x
		
	# Check Space and Shift for vertical (Up/Down) movement
	if Input.is_physical_key_pressed(KEY_SPACE):
		direction += Vector3.UP
	if Input.is_physical_key_pressed(KEY_SHIFT):
		direction -= Vector3.UP
		
	# Normalize the direction so moving diagonally isn't faster
	if direction != Vector3.ZERO:
		direction = direction.normalized()
		
	# Move the camera
	position += direction * move_speed * delta
