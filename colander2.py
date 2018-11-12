import colander

friend = colander.SchemaNode(colander.Tuple())
friend.add(colander.SchemaNode(colander.Int(),
                               validator=colander.Range(0, 9999),
           name='rank'))
friend.add(colander.SchemaNode(colander.String(), name='name'))

print(friend.typ)
for each_p in friend:
    print(each_p.typ)


phone = colander.SchemaNode(
    colander.Mapping(),
    colander.SchemaNode(
        colander.String(),
        validator=colander.OneOf(['home', 'work']),
        name='location'))
phone.add(colander.SchemaNode(colander.String(), name='number'))

print(phone.typ)
for each_p in phone:
    print(each_p.typ)

schema = colander.SchemaNode(colander.Mapping())
schema.add(colander.SchemaNode(colander.String(), name='name'))
schema.add(colander.SchemaNode(colander.Int(), name='age',
                               validator=colander.Range(0, 200)))
schema.add(colander.SequenceSchema(friend, name='friends'))
schema.add(colander.SequenceSchema(phone, name='phones'))

print(schema.typ)
for each_schema in schema:
    print(each_schema.typ)