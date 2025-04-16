import flet as ft

class Signup(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page 
        
        page.title = "Sign Up Page"
        page.window.max_width = 580
        page.window.max_height = 740
        page.padding = 0

        self.content = ft.Container(
            width=580,
            height=740,
            gradient= ft.LinearGradient(['#333399','#eafafe']),
            content = ft.Container(
                ft.Container(
                    ft.Stack([
                        ft.Container(    
                            border_radius= 11,
                            rotate=ft.Rotate(0.98*3.14), #degree
                            width=360,
                            height=620,
                            bgcolor='#22ffffff',
                            
                        ),
                        ft.Container(
                            ft.Text(
                                "Sign Up",
                                width=360,
                                size=30,
                                weight='w900',
                                color='#0a4757',
                                text_align='center',
                            
                            ),
                            top=30,

                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='First Name',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.PERSON,

                                    ),

                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Surname',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.PERSON,

                                    ),
                                 
                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Email',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.EMAIL_OUTLINED,

                                    ),

                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Phone Number',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.EMAIL_OUTLINED,

                                    ),

                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Address',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.PERSON,

                                    ),

                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Password',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.PERSON,

                                    ),

                                    ft.TextField(
                                        width=280,
                                        height=40,
                                        hint_text='Confirm Password',
                                        border='underline',
                                        color='#303030',
                                        # prefix_icon= ft.Icons.PERSON,

                                    ),
                                    ft.Container(
                                        ft.ElevatedButton(
                                                content= ft.Text(
                                                    "Submit", 
                                                    color= 'white',
                                                    weight='w500',
                                                ),
                                                width=180,
                                                bgcolor = '#0a4757',
                                                on_click = lambda e: self.page\
                                                    .go("pages/authentication/login")        
                                            ),
                                            padding= ft.padding.only(45,30),
                                            
                                    ),
                                    
                                ],
                            ),    
                            padding= ft.padding.only(top=100, left=40),
                            width=360,
                            height=620,
                            bgcolor='#22ffffff',
                            border_radius= 11,
                        ),
                        
                    ]),
                

                ),
                padding=ft.padding.only(top=40, left=105),
                width=360,
                height=620,
                

                ),   
                
            )

    


        
