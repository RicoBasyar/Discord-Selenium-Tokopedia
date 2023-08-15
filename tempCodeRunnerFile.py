async def search(ctx, *,search):
    search_result = await open_search_tokped(search)

    message = '**Hasil pencarian :\n**'

    for name, price in search_result:
        message = message + f'`{name} - {price}`\n\n'

    await ctx.send(message)