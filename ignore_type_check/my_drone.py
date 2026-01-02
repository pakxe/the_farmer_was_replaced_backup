def my_spawn_drone(fn, arg):
    def callback():
        fn(arg)

    return spawn_drone(callback)

