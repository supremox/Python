import flet as ft

class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page 
        
        page.title = "Login Page"
        page.window.max_width = 580
        page.window.max_height = 740
        page.window.resizable = False
        page.padding = 0

        self.text_username = ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Username',
                            border='underline',
                            color='#303030',
                            prefix_icon= ft.Icons.EMAIL,
                            # on_change= self.validate
                        )
        
        self.text_password = ft.TextField(
                            width=280,
                            height=40,
                            hint_text='Password',
                            border='underline',
                            color='#303030',
                            prefix_icon= ft.Icons.LOCK,
                            password=True,
                            # on_change= self.validate

                        )
        
        self.button_login = ft.ElevatedButton(
                            content= ft.Text(
                                "Login", 
                                color= 'white',
                                weight='w500',
                            ),
                            width=280,
                            bgcolor = '#0a4757',
                            on_click= self.validate,
                            # on_click = lambda e: self.page\
                            #     .go("pages/dashboard/test")        
                        )
        
        self.alert_dialog = ft.AlertDialog(
                shape=ft.RoundedRectangleBorder(20),
                title=ft.Column(
                    controls=[
                        ft.Container(
                            ft.Icon(ft.Icons.WARNING, color=ft.Colors.RED),
                            padding= ft.padding.only(120,5),
                        ),
                        
                        ft.Text(
                            "Input Username and Password!",
                            size=20,
                        )

                    ]
                ),
            )

        self.content = ft.Container(
            width=580,
            height=740,
            gradient= ft.LinearGradient(['#333399','#eafafe']),
            content = ft.Container(
                ft.Stack([
                    ft.Container(
                        border_radius= 11,
                        rotate=ft.Rotate(0.98*3.14), #degree
                        width=360,
                        height=560,
                        bgcolor='#22ffffff',
                    ),
                    ft.Container(
                        ft.Container(
                            ft.Column([
                            ft.Container(
                                ft.Image(
                                    src='src\\assets\\images\\icon.png',
                                    width=50
                                ),
                                padding= ft.padding.only(150,20),
                            ),
                            ft.Text(
                                "Login",
                                width=360,
                                size=30,
                                weight='w900',
                                text_align='center'
                                
                            ),
                            ft.Container(
                                self.text_username,
                                padding= ft.padding.only(25,20),
                            ), 
                            ft.Container(
                                self.text_password,
                                padding= ft.padding.all(25),
                            ), 
                            ft.Container(
                                ft.TextButton(
                                    "I forgot my password!",
                                ),
                                padding= ft.padding.only(25),
                            ),
                            ft.Container(
                                self.button_login,
                                padding= ft.padding.only(40,10),
                                    
                            ),
                            ft.Container(
                                ft.Row([
                                        ft.Text(
                                            "don't have an account?",

                                        ),
                                        ft.TextButton(
                                            "Create a free account.",
                                            on_click = lambda e: self.page\
                                                    .go("pages/authentication/signup")
                                        ),
                                ], 
                                spacing=0
                                ),
                                padding= ft.padding.only(40)
                            )  
                            

                            ]),

                        ),
                        width=360,
                        height=560,
                        bgcolor='#22ffffff',
                        border_radius= 11,
                    )
                ]),

            padding=110,
            width=360,
            height=560,
            )
        )


    def validate(self, e: ft.ControlEvent) -> None:
        if all([self.text_username.value, self.text_password.value]):
            self.page.go('pages/dashboard/test')
            print('Username:', self.text_username.value)
            print('Password:', self.text_password.value)

        self.page.open(self.alert_dialog)
            
            

            


            
    

       
