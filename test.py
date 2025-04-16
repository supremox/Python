import flet as ft

class UIPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)

        self.page = page 

        self.page.title = "User Dashboard"
        self.page.padding = 0 

        self.color_blue = "#73b1fc"
        self.color_purple = "#bb7efd"
        self.bg_color = "#3f3965"
        self.container_color = "#5864af"
        self.color_navigation_btn = "#6185d4"
        self.color1_card = "#f46fd8"
        self.color2_card = "#64e4ed"
        
        self.page.bgcolor = self.bg_color

        self.animation_style = ft.animation.Animation(500, ft.AnimationCurve.EASE_IN_TO_LINEAR)

        # self.mode_switch = ft.Switch(
        #                         value=True,
        #                         label= "Dark",
        #                         on_change= self.mode_change_update,
        #                         track_color= self.color_purple,
        #                         thumb_icon={
        #                             ft.ControlState.DEFAULT: ft.Icons.LIGHT_MODE,
        #                             ft.ControlState.SELECTED: ft.Icons.DARK_MODE,
        #                         },
        #                     ),

        self.container_1 =ft.Container(
                                expand=True,
                                # bgcolor= self.container_color,
                                offset= ft.transform.Offset(0,0),
                                animate_offset= self.animation_style,
                                margin=15,
                                border_radius=10,
                                content= ft.Row(
                                    controls=[
                                        ft.Container(
                                            expand=True,
                                            content= ft.Stack(
                                                alignment= ft.alignment.top_center,
                                                controls=[
                                                    ft.Container(
                                                        expand=True,
                                                        bgcolor= self.container_color,
                                                        margin= ft.margin.only(left=0, top=150, right=0, bottom=0),
                                                        padding= ft.padding.only(left=0, top=100, right=0, bottom=0),
                                                        border_radius=20,
                                                        content= ft.Column(
                                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text("Transfer", color='white', size=20, weight='bold'),
                                                                ft.Tabs(
                                                                    tab_alignment= ft.TabAlignment.CENTER,
                                                                    indicator_color= self.color_purple,
                                                                    label_color='white',
                                                                    indicator_tab_size=True,
                                                                    expand=True,
                                                                    tabs=[
                                                                        ft.Tab(
                                                                            "To send",                                                                           
                                                                            content= ft.Container(
                                                                                padding = 20,
                                                                                content= ft.Column(
                                                                                    spacing=10,
                                                                                    controls=[
                                                                                       ft.Text(
                                                                                           "Pay Now",
                                                                                           color='white',
                                                                                           size=15,
                                                                                       ),
                                                                                       ft.TextField(
                                                                                           expand=True,
                                                                                           hint_text="1234 4563 1235 4566",
                                                                                           border_color="transparent",
                                                                                           border_radius=10,
                                                                                           bgcolor= self.bg_color,
                                                                                       ),
                                                                                       ft.Row(
                                                                                          controls=[
                                                                                            ft.Column(
                                                                                                expand=True,
                                                                                                controls=[
                                                                                                    ft.Text(
                                                                                                        "Amount",
                                                                                                        color='white',
                                                                                                        size=15,
                                                                                                    ),
                                                                                                    ft.TextField(
                                                                                                        hint_text="$ 500.00",
                                                                                                        border_color='transparent',
                                                                                                        bgcolor= self.bg_color,
                                                                                                        border_radius=10,
                                                                                                    ),
                                                                                                ],

                                                                                            ),
                                                                                            ft.Column(
                                                                                                expand=True,
                                                                                                controls=[
                                                                                                    ft.Text(
                                                                                                        "Comments",
                                                                                                        color='white',
                                                                                                        size=15,
                                                                                                    ),
                                                                                                    ft.TextField(
                                                                                                        hint_text=".....",
                                                                                                        border_color='transparent',
                                                                                                        bgcolor= self.bg_color,
                                                                                                        border_radius=10,
                                                                                                    ),
                                                                                                ],

                                                                                            ),
                                                                                          ], 
                                                                                       ), 
                                                                                       ft.Row(
                                                                                           expand=True,
                                                                                           controls=[
                                                                                               ft.Text("Commission: $ 2.00", color='white',size=15,),
                                                                                               ft.Text("Total: $ 502.00", color='white',size=15,),
                                                                                           ],
                                                                                       ),
                                                                                       ft.Column(
                                                                                           controls=[
                                                                                               ft.Container(
                                                                                                   height=50,
                                                                                                   border_radius=20,
                                                                                                   gradient= ft.LinearGradient(
                                                                                                       colors=[
                                                                                                        self.color1_card,
                                                                                                        self.color_purple,
                                                                                                        self.color2_card,  
                                                                                                       ],
                                                                                                   ),
                                                                                                   content=ft.Row(
                                                                                                       alignment= ft.MainAxisAlignment.CENTER,
                                                                                                       controls= [
                                                                                                           ft.Icon(ft.Icons.SEND, color='white'),
                                                                                                       ],

                                                                                                   ),
                                                                                               ),
                                                                                           ],
                                                                                       ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        ft.Tab(
                                                                            "Application",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    ft.Container(
                                                        height=180,
                                                        width=300,
                                                        gradient= ft.LinearGradient(
                                                            rotation=0.5,
                                                            colors=[
                                                                self.color1_card,
                                                                self.color2_card,
                                                                self.color_purple,
                                                            ]
                                                        ),
                                                        margin= ft.margin.only(left=50, top=50, bottom=0),
                                                        border_radius=20,
                                                        padding=10,
                                                        content= ft.Column(
                                                            controls=[
                                                                ft.Text("1234 4563 1235 4566", color='white', size=16),
                                                                ft.Text("$ 10, 870.00", color='white', size=30, weight='bold'),
                                                                ft.Container(
                                                                    ft.Text("Vincent Carl Calidguid", color='white', size= 18, weight='bold'),
                                                                    margin= ft.margin.only(left=5, top=40, bottom=10),
                                                                ),
                                                                
                                                            ],
                                                        ),
                                                    ),                  
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            expand=True,
                                            content= ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        height=50,
                                                        controls=[
                                                            ft.Container(
                                                                expand=True,
                                                                border_radius=20,
                                                                bgcolor= self.container_color,
                                                                content= ft.TextField(
                                                                    hint_text= "Search",
                                                                    border_radius=20,
                                                                    border_color='transparent',
                                                                    suffix_icon= ft.Icons.SEARCH,
                                                                ),

                                                            ),
                                                            ft.Container(
                                                                bgcolor= self.container_color,
                                                                border_radius=20,
                                                                width=50,
                                                                height=50,
                                                                alignment = ft.alignment.center,
                                                                content= ft.Icon(
                                                                    name=ft.Icons.NOTIFICATIONS_OUTLINED, 
                                                                    color='white',
                                                                    badge= ft.Badge(
                                                                        small_size=10,
                                                                        alignment=ft.alignment.top_center,
                                                                        bgcolor= self.color1_card,
                                                                        text="21",
                                                                    ),
                                                                    
                                                                ),  
                                                            ),
                                                            ft.Container(
                                                                bgcolor= self.container_color,
                                                                border_radius=20,
                                                                width=50,
                                                                height=50,
                                                                content= ft.Icon(name=ft.Icons.PERSON_ROUNDED, color='white'),
                                                            ),
                                                        ],
                                                    ),
                                                    ft.Container(
                                                        bgcolor=self.color_purple,
                                                        padding=20,
                                                        expand=True,
                                                        border_radius=20,
                                                        content= ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "balance",
                                                                            size=20,
                                                                            weight='bold',
                                                                        ),
                                                                        ft.Container(
                                                                            border_radius=10,
                                                                            bgcolor=ft.Colors.with_opacity(0.3, self.bg_color),
                                                                            width=40,
                                                                            height=30,
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.Text(
                                                                                value="$",
                                                                                size=15,
                                                                            )

                                                                        ),

                                                                    ],
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Text(
                                                                            "$ 7, 830.00",
                                                                            size=25,
                                                                            weight='bold',
                                                                        ),
                                                                        ft.Container(
                                                                            border_radius=10,
                                                                            bgcolor='transaprent',
                                                                            border= ft.border.all(1, "white"),
                                                                            width=40,
                                                                            height=30,
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.Text(
                                                                                value="$",
                                                                                size=15,
                                                                            )

                                                                        ),

                                                                    ],
                                                                ),

                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Container(
                                                                            border_radius=10,
                                                                            bgcolor=ft.Colors.with_opacity(0.3, self.bg_color),
                                                                            width=40,
                                                                            height=30,
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.Icon(name=ft.Icons.ARROW_UPWARD, color='white')

                                                                        ),
                                                                        ft.Text("+ $ 9,840.00", size=15),

                                                                        ft.Container(
                                                                            border_radius=10,
                                                                            bgcolor=ft.Colors.with_opacity(0.3, self.bg_color),
                                                                            width=40,
                                                                            height=30,
                                                                            alignment=ft.alignment.center,
                                                                            content=ft.Icon(name=ft.Icons.ARROW_DOWNWARD, color='white')

                                                                        ),
                                                                        ft.Text("- $ 2,130.00", size=15),

                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    ft.Container(
                                                        expand=True,
                                                        bgcolor=self.container_color,
                                                        border_radius=20,
                                                        padding=20,
                                                        content= ft.Column(
                                                            expand=True,
                                                            controls=[
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Text("Information", size=16, weight='bold', color='white'),
                                                                        ft.IconButton(icon=ft.Icons.EDIT, icon_color='white'),

                                                                    ],
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                    controls=[     
                                                                        ft.Icon(name=ft.Icons.LOCATION_CITY, color='white'),
                                                                        ft.Text("Place: Manila", size=16, color='white'),
                                                                    ],
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                    controls=[     
                                                                        ft.Icon(name=ft.Icons.LOCATION_ON_OUTLINED, color='white'),
                                                                        ft.Text("Direction: Philippines", size=16, color='white'),
                                                                    ],
                                                                ),
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                    controls=[     
                                                                        ft.Icon(name=ft.Icons.CREDIT_CARD, color='white'),
                                                                        ft.Text("ID Card: 1234 4563 1235 4566", size=16, color='white'),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),

                                                    ),
                                                    ft.Container(
                                                        expand=True,
                                                        bgcolor=self.container_color,
                                                        border_radius=20,
                                                        padding=20,
                                                        content= ft.Column(
                                                            controls= [
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Text("Security", size=16, weight='bold', color='white'),
                                                                        ft.IconButton(icon=ft.Icons.MORE_HORIZ, icon_color='white'),

                                                                    ],
                                                                ),
                                                                ft.Row(
                                                                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Row(
                                                                            controls=[
                                                                                ft.Container(
                                                                                    border_radius=20,
                                                                                    bgcolor= self.bg_color,
                                                                                    height= 50,
                                                                                    width=50,
                                                                                    content= ft.Icon(
                                                                                        name=ft.Icons.VERIFIED_USER,
                                                                                        color='white',
                                                                                    ),
                                                                                ),
                                                                                ft.Text("2FA Enabled", size=16, color='white'),
                                                                            ],
                                                                        ),
                                                                        ft.Switch(
                                                                            value=True,
                                                                            active_color= self.color1_card,
                                                                            track_color= self.color2_card,
                                                                            thumb_icon={
                                                                                ft.ControlState.DEFAULT: ft.Icons.CLOSE,
                                                                                ft.ControlState.SELECTED: ft.Icons.CHECK,
                                                                            },
                                                                        ),
                                                                    ],
                                                                ),

                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                    controls=[
                                                                        ft.Row(
                                                                            controls=[
                                                                               ft.Container(
                                                                                    border_radius=20,
                                                                                    bgcolor= self.bg_color,
                                                                                    height= 50,
                                                                                    width=50,
                                                                                    content= ft.Icon(name=ft.Icons.LOCK, color='white',),          
                                                                                ), 
                                                                                ft.Text("Password", size=16, color='white'),
                                                                            ],
                                                                        ),
                                                                        ft.ElevatedButton(
                                                                            text="Load", 
                                                                            bgcolor= self.container_color,
                                                                            style= ft.ButtonStyle(
                                                                                color='white',
                                                                                side= ft.BorderSide(1, "white"),
                                                                    
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),

                                                        
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ]
                                )
                            )
        
        self.container_2 =ft.Container(
                                expand=True,
                                bgcolor= self.container_color,
                                offset= ft.transform.Offset(2,0),
                                animate_offset= self.animation_style,
                            )
        self.container_3 =ft.Container(
                                expand=True,
                                bgcolor= self.container_color,
                                offset= ft.transform.Offset(2,0),
                                animate_offset= self.animation_style,
                            )
        self.container_4 =ft.Container(
                                expand=True,
                                bgcolor= self.container_color,
                                offset= ft.transform.Offset(2,0),
                                animate_offset= self.animation_style,
                            )


        self.frame = ft.Container(
            expand=True,
            content = ft.Stack(
                controls=[
                    self.container_1,
                    self.container_2,
                    self.container_3,
                    self.container_4,
                ]

            ),
        )

        self.option_1 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_btn,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,1),
            height=40,
            content=ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.DIRECTIONS, color='white'),
                    ft.Text("Inicio", width=120, color='white')
                ]
            )
        )

        self.option_2 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_btn,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,2),
            height=40,
            content=ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.SEARCH, color='white'),
                    ft.Text("Search", width=120, color='white')
                ]
            )
        )

        self.option_3 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_btn,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,3),
            height=40,
            content=ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.AIRPLANEMODE_ON, color='white'),
                    ft.Text("Location", width=120, color='white')
                ]
            )
        )

        self.option_4 = ft.Container(
            padding=10,
            bgcolor= self.color_navigation_btn,
            border_radius=15,
            offset= ft.transform.Offset(0,0),
            animate_offset= self.animation_style,
            on_click=lambda e: self.change_page(e,4),
            height=40,
            content=ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.SETTINGS, color='white'),
                    ft.Text("Settings", width=120, color='white')
                ]
            )
        )

        self.navigation = ft.Container(
            padding=20,
            bgcolor=self.container_color,
            animate_size= self.animation_style,
            content= ft.Column(
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    self.option_1,
                    self.option_2,
                    self.option_3,
                    self.option_4,
                    # self.mode_switch,

                ],
            ),
        )

        self.switch_control = {
            1: self.container_1,
            2: self.container_2,
            3: self.container_3,
            4: self.container_4, 
        }


        self.page.add(
            ft.Row(
                expand=True,
                spacing=20,
                controls=[
                    self.navigation,
                    self.frame,
                ],
            )
        )

    def change_page(self, e, n):
        for page in self.switch_control:
            self.switch_control[page].offset.y =  2
            self.option_1.bgcolor = self.color_navigation_btn
            self.option_2.bgcolor = self.color_navigation_btn
            self.option_3.bgcolor = self.color_navigation_btn
            self.option_4.bgcolor = self.color_navigation_btn

        if n==1:
            self.option_1.offset.x = 0.15
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
            self.option_1.bgcolor = self.color_purple
            self.option_1.update()

        if n==2:
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0.15
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0
            self.option_2.bgcolor = self.color_purple
            self.option_2.update()

        if n==3:
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0.15
            self.option_4.offset.x = 0
            self.option_3.bgcolor = self.color_purple
            self.option_3.update()

        if n==4:
            self.option_1.offset.x = 0
            self.option_2.offset.x = 0
            self.option_3.offset.x = 0
            self.option_4.offset.x = 0.15
            self.option_4.bgcolor = self.color_purple
            self.option_4.update()

        self.switch_control[n].offset.y =  0

        self.page.update()


    # def mode_change_update(self, e):
    #     if e.data == "False":
    #         self.mode_switch.label ="Light"
    #     else:
    #         self.mode_switch.label = "Dark"

    #     self.page.update()




ft.app(target=lambda page: UIPage(page))