
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstname)<3:
            flash('Username must be greater than 2 characters', category='error')
        elif len(password)<7:
            flash('Password