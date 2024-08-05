from flet import *

def main(page: Page):
    page.window.width=400
    page.window.height=700
    tasks=[]
    text_screen= TextField(label="Enter Your Task",width=290,border_color=colors.BLUE_GREY_50)
    def delete_task(event):
        for i in tasks:
            if event.control in i.content.controls[1].controls:
                tasks.remove(i)
                page.update()
                break
    def add_task():
        task_Name = text_screen.value
        text_screen.value=""
        tasks.append(Container(
            content=Row(controls=[Row(controls=[
            Checkbox(value=True),Text(value=task_Name)
        ]),Row(controls=[IconButton(icon=icons.DELETE,on_click=delete_task,style=ButtonStyle(color=colors.RED)),IconButton(icon=icons.EDIT,on_click=edit_task)])],alignment=MainAxisAlignment.SPACE_BETWEEN),
            width=450,
            height=50,
            bgcolor=colors.with_opacity(0.25, '#FFFFFF'),
            border_radius=border_radius.all(10),                   # Border radius
            border=border.all(1, color=colors.with_opacity(0.18,'#FFFFFF')),
            shadow=BoxShadow(
                color='#1F26875E',  # Shadow color
                blur_radius=32,                 # Blur radius
                offset=Offset(0, 8),
            ) 

        ))
        page.update()
    def to_update(task,name):
        for i in range(0,len(tasks)):
            if task==tasks[i]:
                tasks[i].content.controls[0].controls[1].value=name
                page.update()
                break
        page.go('/')
    def get_name():
        return updateContainer.content.controls[1].controls[0].value
    def edit_task(event):
        for i in tasks:
            if event.control in i.content.controls[1].controls:
                break
        updateContainer.content.controls[1].controls[0].value=i.content.controls[0].controls[1].value
        updateContainer.content.controls[1].controls[1].on_click=lambda _:to_update(i,get_name())
        page.update()
        page.go('/update')
    def on_route_c(route):
        page.views.clear()
        page.views.append(pages[page.route])
    container= Container(
        width = 500,
        height = 645,
        bgcolor=colors.BLUE_300,
        border=border.all(width=3,color=colors.BLACK),
        border_radius=border_radius.all(20),
        padding=padding.all(10),
        content=Container(
            width=480,
            height=625,
            content=Column(controls=[

                Row(controls=[Text(value='To Do List',col=colors.WHITE,size=35)],alignment=MainAxisAlignment.START),
                Container(
                    margin=margin.only(top=20),
                    content=Row(controls=[text_screen,IconButton(icons.ADD,on_click=lambda _:add_task(),style=ButtonStyle(color=colors.BLUE_700,bgcolor=colors.GREY_300))])),
                Container(
                    margin=margin.only(top=20),
                    content=Text(value='Your Tasks',size=25)
                ),
                Container(
                    margin=margin.only(top=10),
                    height=400,
                    content=Column(controls=tasks,scroll='auto'),
                )
            ])
        )
    )
    updateContainer=Container(
        content=Column(
            controls=[
                Text(value='Task'),
                Row(controls=[TextField(value="sadasd"),IconButton(icon=icons.ADD_CIRCLE)])
            ]
        )
    )
    page.add(container)
    pages={
        '/':View('/',[container]),'/update':
        View('/update',[updateContainer])
    }
    page.on_route_change=on_route_c
app(target=main)