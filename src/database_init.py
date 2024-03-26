def check():
    with session_factory() as session:
        ben = User(username="ben", password='pass')
        tom = User(username="tom", password='pass')
        # создаем пользователей
        note1 = Note(title="note11111", body="dsfsfsfsdf", datetime="fsdfsdffsf")
        note2 = Note(title="note22222", body="dsfsfsfsdf", datetime="fsdfsdffsf")
        # устанавливаем для компаний списки пользователей
        tom.notes = [note1, note2]
        # добавляем компании в базу данных, и вместе с ними добавляются пользователи
        session.add(tom)
        session.commit()

        query = select(User)

        result = session.execute(query)

        result = result.scalars().all()

        print(result[0].username)
        for note in result[0].notes:
            print(note.title)
