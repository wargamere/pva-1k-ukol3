def my_function():
    import emoji
    print("yo" + emoji.emojize(":thumbs_up:", language='alias'))

    selected_emoji = input("pick a emoji (e.g. :thumbs_up:): ")

    print(emoji.emojize(selected_emoji, language='alias'))

myfunction()
