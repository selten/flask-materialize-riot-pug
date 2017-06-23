test
    div.col.s12.m6
        div.row
            div.col.s4.center(
                each="{num in data}"
            )
                span {num}

    script(type="text/coffeescript").
        self = @

        @on 'mount', ->
            self.data = ['1', '2', '3']
            self.update({data: self.data})