def my_spawn_drone(fn, arg):
    def callback():
        fn(arg)

    spawn_drone(callback)