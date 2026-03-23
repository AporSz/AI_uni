extends CanvasLayer

# We will drag our Spawner node into this slot in the Inspector!
@export var spawner: Node3D 

@onready var count_label = $PanelContainer/VBoxContainer/countlabel
@onready var count_slider = $PanelContainer/VBoxContainer/countslider
@onready var speed_label = $PanelContainer/VBoxContainer/speedlabel
@onready var speed_slider = $PanelContainer/VBoxContainer/speedslider
@onready var restart_button = $PanelContainer/VBoxContainer/restartbutton

func _ready():
	# Configure the Count Slider (1 to 1000 particles)
	count_slider.min_value = 1
	count_slider.max_value = 1000
	count_slider.value = 100
	
	# Configure the Speed Slider (1.0 to 50.0 speed)
	speed_slider.min_value = 1.0
	speed_slider.max_value = 50.0
	speed_slider.step = 0.5
	speed_slider.value = 10.0
	
	# Connect the UI signals so they run our functions below
	count_slider.value_changed.connect(_on_count_changed)
	speed_slider.value_changed.connect(_on_speed_changed)
	restart_button.pressed.connect(_on_restart_pressed)
	
	# Set the text for the very first frame
	_on_count_changed(count_slider.value)
	_on_speed_changed(speed_slider.value)

func _on_count_changed(value: float):
	count_label.text = "Particle Count: " + str(int(value))

func _on_speed_changed(value: float):
	speed_label.text = "Initial Speed: " + str(value) + " m/s"

func _on_restart_pressed():
	if spawner:
		# Tell the spawner to wipe the board and start over with the new numbers
		spawner.restart_sim(int(count_slider.value), speed_slider.value)
