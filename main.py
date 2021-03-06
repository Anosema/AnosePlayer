from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QPushButton, QProgressBar, QMenu
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtCore import Qt, QUrl

from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent

from sys import argv, exit
from os.path import abspath, isfile

icons = {'ti-wand': '\ue600', 'ti-volume': '\ue601', 'ti-user': '\ue602', 'ti-unlock': '\ue603', 'ti-unlink': '\ue604', 'ti-trash': '\ue605', 'ti-thought': '\ue606', 'ti-target': '\ue607', 'ti-tag': '\ue608', 'ti-tablet': '\ue609', 'ti-star': '\ue60a', 'ti-spray': '\ue60b', 'ti-signal': '\ue60c', 'ti-shopping-cart': '\ue60d', 'ti-shopping-cart-full': '\ue60e', 'ti-settings': '\ue60f', 'ti-search': '\ue610', 'ti-zoom-in': '\ue611', 'ti-zoom-out': '\ue612', 'ti-cut': '\ue613', 'ti-ruler': '\ue614', 'ti-ruler-pencil': '\ue615', 'ti-ruler-alt': '\ue616', 'ti-bookmark': '\ue617', 'ti-bookmark-alt': '\ue618', 'ti-reload': '\ue619', 'ti-plus': '\ue61a', 'ti-pin': '\ue61b', 'ti-pencil': '\ue61c', 'ti-pencil-alt': '\ue61d', 'ti-paint-roller': '\ue61e', 'ti-paint-bucket': '\ue61f', 'ti-na': '\ue620', 'ti-mobile': '\ue621', 'ti-minus': '\ue622', 'ti-medall': '\ue623', 'ti-medall-alt': '\ue624', 'ti-marker': '\ue625', 'ti-marker-alt': '\ue626', 'ti-arrow-up': '\ue627', 'ti-arrow-right': '\ue628', 'ti-arrow-left': '\ue629', 'ti-arrow-down': '\ue62a', 'ti-lock': '\ue62b', 'ti-location-arrow': '\ue62c', 'ti-link': '\ue62d', 'ti-layout': '\ue62e', 'ti-layers': '\ue62f', 'ti-layers-alt': '\ue630', 'ti-key': '\ue631', 'ti-import': '\ue632', 'ti-image': '\ue633', 'ti-heart': '\ue634', 'ti-heart-broken': '\ue635', 'ti-hand-stop': '\ue636', 'ti-hand-open': '\ue637', 'ti-hand-drag': '\ue638', 'ti-folder': '\ue639', 'ti-flag': '\ue63a', 'ti-flag-alt': '\ue63b', 'ti-flag-alt-2': '\ue63c', 'ti-eye': '\ue63d', 'ti-export': '\ue63e', 'ti-exchange-vertical': '\ue63f', 'ti-desktop': '\ue640', 'ti-cup': '\ue641', 'ti-crown': '\ue642', 'ti-comments': '\ue643', 'ti-comment': '\ue644', 'ti-comment-alt': '\ue645', 'ti-close': '\ue646', 'ti-clip': '\ue647', 'ti-angle-up': '\ue648', 'ti-angle-right': '\ue649', 'ti-angle-left': '\ue64a', 'ti-angle-down': '\ue64b', 'ti-check': '\ue64c', 'ti-check-box': '\ue64d', 'ti-camera': '\ue64e', 'ti-announcement': '\ue64f', 'ti-brush': '\ue650', 'ti-briefcase': '\ue651', 'ti-bolt': '\ue652', 'ti-bolt-alt': '\ue653', 'ti-blackboard': '\ue654', 'ti-bag': '\ue655', 'ti-move': '\ue656', 'ti-arrows-vertical': '\ue657', 'ti-arrows-horizontal': '\ue658', 'ti-fullscreen': '\ue659', 'ti-arrow-top-right': '\ue65a', 'ti-arrow-top-left': '\ue65b', 'ti-arrow-circle-up': '\ue65c', 'ti-arrow-circle-right': '\ue65d', 'ti-arrow-circle-left': '\ue65e', 'ti-arrow-circle-down': '\ue65f', 'ti-angle-double-up': '\ue660', 'ti-angle-double-right': '\ue661', 'ti-angle-double-left': '\ue662', 'ti-angle-double-down': '\ue663', 'ti-zip': '\ue664', 'ti-world': '\ue665', 'ti-wheelchair': '\ue666', 'ti-view-list': '\ue667', 'ti-view-list-alt': '\ue668', 'ti-view-grid': '\ue669', 'ti-uppercase': '\ue66a', 'ti-upload': '\ue66b', 'ti-underline': '\ue66c', 'ti-truck': '\ue66d', 'ti-timer': '\ue66e', 'ti-ticket': '\ue66f', 'ti-thumb-up': '\ue670', 'ti-thumb-down': '\ue671', 'ti-text': '\ue672', 'ti-stats-up': '\ue673', 'ti-stats-down': '\ue674', 'ti-split-v': '\ue675', 'ti-split-h': '\ue676', 'ti-smallcap': '\ue677', 'ti-shine': '\ue678', 'ti-shift-right': '\ue679', 'ti-shift-left': '\ue67a', 'ti-shield': '\ue67b', 'ti-notepad': '\ue67c', 'ti-server': '\ue67d', 'ti-quote-right': '\ue67e', 'ti-quote-left': '\ue67f', 'ti-pulse': '\ue680', 'ti-printer': '\ue681', 'ti-power-off': '\ue682', 'ti-plug': '\ue683', 'ti-pie-chart': '\ue684', 'ti-paragraph': '\ue685', 'ti-panel': '\ue686', 'ti-package': '\ue687', 'ti-music': '\ue688', 'ti-music-alt': '\ue689', 'ti-mouse': '\ue68a', 'ti-mouse-alt': '\ue68b', 'ti-money': '\ue68c', 'ti-microphone': '\ue68d', 'ti-menu': '\ue68e', 'ti-menu-alt': '\ue68f', 'ti-map': '\ue690', 'ti-map-alt': '\ue691', 'ti-loop': '\ue692', 'ti-location-pin': '\ue693', 'ti-list': '\ue694', 'ti-light-bulb': '\ue695', 'ti-Italic': '\ue696', 'ti-info': '\ue697', 'ti-infinite': '\ue698', 'ti-id-badge': '\ue699', 'ti-hummer': '\ue69a', 'ti-home': '\ue69b', 'ti-help': '\ue69c', 'ti-headphone': '\ue69d', 'ti-harddrives': '\ue69e', 'ti-harddrive': '\ue69f', 'ti-gift': '\ue6a0', 'ti-game': '\ue6a1', 'ti-filter': '\ue6a2', 'ti-files': '\ue6a3', 'ti-file': '\ue6a4', 'ti-eraser': '\ue6a5', 'ti-envelope': '\ue6a6', 'ti-download': '\ue6a7', 'ti-direction': '\ue6a8', 'ti-direction-alt': '\ue6a9', 'ti-dashboard': '\ue6aa', 'ti-control-stop': '\ue6ab', 'ti-control-shuffle': '\ue6ac', 'ti-control-play': '\ue6ad', 'ti-control-pause': '\ue6ae', 'ti-control-forward': '\ue6af', 'ti-control-backward': '\ue6b0', 'ti-cloud': '\ue6b1', 'ti-cloud-up': '\ue6b2', 'ti-cloud-down': '\ue6b3', 'ti-clipboard': '\ue6b4', 'ti-car': '\ue6b5', 'ti-calendar': '\ue6b6', 'ti-book': '\ue6b7', 'ti-bell': '\ue6b8', 'ti-basketball': '\ue6b9', 'ti-bar-chart': '\ue6ba', 'ti-bar-chart-alt': '\ue6bb', 'ti-back-right': '\ue6bc', 'ti-back-left': '\ue6bd', 'ti-arrows-corner': '\ue6be', 'ti-archive': '\ue6bf', 'ti-anchor': '\ue6c0', 'ti-align-right': '\ue6c1', 'ti-align-left': '\ue6c2', 'ti-align-justify': '\ue6c3', 'ti-align-center': '\ue6c4', 'ti-alert': '\ue6c5', 'ti-alarm-clock': '\ue6c6', 'ti-agenda': '\ue6c7', 'ti-write': '\ue6c8', 'ti-window': '\ue6c9', 'ti-widgetized': '\ue6ca', 'ti-widget': '\ue6cb', 'ti-widget-alt': '\ue6cc', 'ti-wallet': '\ue6cd', 'ti-video-clapper': '\ue6ce', 'ti-video-camera': '\ue6cf', 'ti-vector': '\ue6d0', 'ti-themify-logo': '\ue6d1', 'ti-themify-favicon': '\ue6d2', 'ti-themify-favicon-alt': '\ue6d3', 'ti-support': '\ue6d4', 'ti-stamp': '\ue6d5', 'ti-split-v-alt': '\ue6d6', 'ti-slice': '\ue6d7', 'ti-shortcode': '\ue6d8', 'ti-shift-right-alt': '\ue6d9', 'ti-shift-left-alt': '\ue6da', 'ti-ruler-alt-2': '\ue6db', 'ti-receipt': '\ue6dc', 'ti-pin2': '\ue6dd', 'ti-pin-alt': '\ue6de', 'ti-pencil-alt2': '\ue6df', 'ti-palette': '\ue6e0', 'ti-more': '\ue6e1', 'ti-more-alt': '\ue6e2', 'ti-microphone-alt': '\ue6e3', 'ti-magnet': '\ue6e4', 'ti-line-double': '\ue6e5', 'ti-line-dotted': '\ue6e6', 'ti-line-dashed': '\ue6e7', 'ti-layout-width-full': '\ue6e8', 'ti-layout-width-default': '\ue6e9', 'ti-layout-width-default-alt': '\ue6ea', 'ti-layout-tab': '\ue6eb', 'ti-layout-tab-window': '\ue6ec', 'ti-layout-tab-v': '\ue6ed', 'ti-layout-tab-min': '\ue6ee', 'ti-layout-slider': '\ue6ef', 'ti-layout-slider-alt': '\ue6f0', 'ti-layout-sidebar-right': '\ue6f1', 'ti-layout-sidebar-none': '\ue6f2', 'ti-layout-sidebar-left': '\ue6f3', 'ti-layout-placeholder': '\ue6f4', 'ti-layout-menu': '\ue6f5', 'ti-layout-menu-v': '\ue6f6', 'ti-layout-menu-separated': '\ue6f7', 'ti-layout-menu-full': '\ue6f8', 'ti-layout-media-right-alt': '\ue6f9', 'ti-layout-media-right': '\ue6fa', 'ti-layout-media-overlay': '\ue6fb', 'ti-layout-media-overlay-alt': '\ue6fc', 'ti-layout-media-overlay-alt-2': '\ue6fd', 'ti-layout-media-left-alt': '\ue6fe', 'ti-layout-media-left': '\ue6ff', 'ti-layout-media-center-alt': '\ue700', 'ti-layout-media-center': '\ue701', 'ti-layout-list-thumb': '\ue702', 'ti-layout-list-thumb-alt': '\ue703', 'ti-layout-list-post': '\ue704', 'ti-layout-list-large-image': '\ue705', 'ti-layout-line-solid': '\ue706', 'ti-layout-grid4': '\ue707', 'ti-layout-grid3': '\ue708', 'ti-layout-grid2': '\ue709', 'ti-layout-grid2-thumb': '\ue70a', 'ti-layout-cta-right': '\ue70b', 'ti-layout-cta-left': '\ue70c', 'ti-layout-cta-center': '\ue70d', 'ti-layout-cta-btn-right': '\ue70e', 'ti-layout-cta-btn-left': '\ue70f', 'ti-layout-column4': '\ue710', 'ti-layout-column3': '\ue711', 'ti-layout-column2': '\ue712', 'ti-layout-accordion-separated': '\ue713', 'ti-layout-accordion-merged': '\ue714', 'ti-layout-accordion-list': '\ue715', 'ti-ink-pen': '\ue716', 'ti-info-alt': '\ue717', 'ti-help-alt': '\ue718', 'ti-headphone-alt': '\ue719', 'ti-hand-point-up': '\ue71a', 'ti-hand-point-right': '\ue71b', 'ti-hand-point-left': '\ue71c', 'ti-hand-point-down': '\ue71d', 'ti-gallery': '\ue71e', 'ti-face-smile': '\ue71f', 'ti-face-sad': '\ue720', 'ti-credit-card': '\ue721', 'ti-control-skip-forward': '\ue722', 'ti-control-skip-backward': '\ue723', 'ti-control-record': '\ue724', 'ti-control-eject': '\ue725', 'ti-comments-smiley': '\ue726', 'ti-brush-alt': '\ue727', 'ti-youtube': '\ue728', 'ti-vimeo': '\ue729', 'ti-twitter': '\ue72a', 'ti-time': '\ue72b', 'ti-tumblr': '\ue72c', 'ti-skype': '\ue72d', 'ti-share': '\ue72e', 'ti-share-alt': '\ue72f', 'ti-rocket': '\ue730', 'ti-pinterest': '\ue731', 'ti-new-window': '\ue732', 'ti-microsoft': '\ue733', 'ti-list-ol': '\ue734', 'ti-linkedin': '\ue735', 'ti-layout-sidebar-2': '\ue736', 'ti-layout-grid4-alt': '\ue737', 'ti-layout-grid3-alt': '\ue738', 'ti-layout-grid2-alt': '\ue739', 'ti-layout-column4-alt': '\ue73a', 'ti-layout-column3-alt': '\ue73b', 'ti-layout-column2-alt': '\ue73c', 'ti-instagram': '\ue73d', 'ti-google': '\ue73e', 'ti-github': '\ue73f', 'ti-flickr': '\ue740', 'ti-facebook': '\ue741', 'ti-dropbox': '\ue742', 'ti-dribbble': '\ue743', 'ti-apple': '\ue744', 'ti-android': '\ue745', 'ti-save': '\ue746', 'ti-save-alt': '\ue747', 'ti-yahoo': '\ue748', 'ti-wordpress': '\ue749', 'ti-vimeo-alt': '\ue74a', 'ti-twitter-alt': '\ue74b', 'ti-tumblr-alt': '\ue74c', 'ti-trello': '\ue74d', 'ti-stack-overflow': '\ue74e', 'ti-soundcloud': '\ue74f', 'ti-sharethis': '\ue750', 'ti-sharethis-alt': '\ue751', 'ti-reddit': '\ue752', 'ti-pinterest-alt': '\ue753', 'ti-microsoft-alt': '\ue754', 'ti-linux': '\ue755', 'ti-jsfiddle': '\ue756', 'ti-joomla': '\ue757', 'ti-html5': '\ue758', 'ti-flickr-alt': '\ue759', 'ti-email': '\ue75a', 'ti-drupal': '\ue75b', 'ti-dropbox-alt': '\ue75c', 'ti-css3': '\ue75d', 'ti-rss': '\ue75e', 'ti-rss-alt': '\ue75f'}


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.playlist = []
		self.files = []

		self.menu = QMenu()
		self.menu.addAction(icons["ti-file"]+" Open a file", lambda:print("file"))
		self.menu.addAction(icons["ti-files"]+" Open a files", lambda:print("files"), "Ctrl+O")
		self.menu.addAction(icons["ti-folder"]+" Open a folder", lambda:print("folder"), "Ctrl+Shift+O")
		self.menu.setStyleSheet("font-family: themify;")

		self.setMinimumSize(500, 60)
		self.move(100, 100)

		self.player = QMediaPlayer()
		self.titleBar = CustomTitleBar(self, "AnosePlayer", "ti-music-alt")
		self.prevBut = QPushButton(icons["ti-control-skip-backward"], self)
		self.pausBut = QPushButton(icons["ti-control-pause"], self)
		self.nextBut = QPushButton(icons["ti-control-skip-forward"], self)
		self.progress = QProgressBar(self)
		self.openFile = QPushButton(icons["ti-plus"], self)

		self.prevBut.setObjectName("Control")
		self.pausBut.setObjectName("Control")
		self.nextBut.setObjectName("Control")
		self.openFile.setObjectName("Control")

		self.progress.setTextVisible(False)
		self.openFile.setMenu(self.menu)
		self.player.setVolume(10)


		self.player.positionChanged.connect(self.updateTime)
		self.player.durationChanged.connect(self.showDuration)
		self.player.mediaChanged.connect(self.changedMedia)
		self.player.volumeChanged.connect(self.showVolume)
		self.player.stateChanged.connect(lambda *args: print(args))
		self.prevBut.clicked.connect(self.previousSong)
		self.pausBut.clicked.connect(self.playPause)
		self.nextBut.clicked.connect(self.nextSong)


		self.player.setMedia(QMediaContent(QUrl.fromLocalFile("/home/martin/Music/Principal/System Of A Down - ATWA.mp3")))


		with open("theme.css", "r") as file: self.setStyleSheet(file.read())

	def oFile(self):
		file = QFileDialog.getExistingDirectory(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
	# def oFiles(self):
	def oFolde(self):
		file = QFileDialog.getExistingDirectory(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")

	def updateTime(self, time):
		self.progress.setValue(time)
		self.progress.repaint()
		print(self.progress.value())
	def showDuration(self, totalTime):
		self.progress.setMaximum(totalTime)
		print(self.progress.maximum())
	def changedMedia(self, *args):
		print(args)
	def showVolume(self, volume):
		print(volume)
	def changeTime(self, time):
		self.player.setPosition(time)
	def previousSong(self):
		if self.i - 1 >= 0:
			self.i -= 1
			self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.playlist[self.i])))
	def playPause(self):
		if self.player.state() == 1:
			self.player.pause()
			self.pausBut.setText(icons["ti-control-play"])
		else:
			self.player.play()
			self.pausBut.setText(icons["ti-control-pause"])
	def nextSong(self):
		if self.i + 1 >= len(self.playlist):
			self.playlist.append(choice(self.files))
		self.i += 1
		self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.playlist[self.i])))



	def resizeEvent(self, e):
		self.titleBar.setGeometry(0, 0, self.width(), 20)
		self.prevBut.setGeometry(0, 20, 30, 30)
		self.pausBut.setGeometry(30, 20, 30, 30)
		self.nextBut.setGeometry(60, 20, 30, 30)
		self.progress.setGeometry(100, 25, 390, 20)
		self.openFile.setGeometry(0, 50, 30, 30)




class CustomTitleBar(QFrame):
	baseStyleSheet = "#TitleBar *{font-family: themify;}#TitleBar #Label{font-size: 16px;}#TitleBar #Min, #TitleBar #Max, #TitleBar #Close{border: 1px solid rgb(21, 21, 21);background-color: rgb(28, 28, 28);color: #E0E0E0E0;padding-left:0px;}"
	def __init__(self, p, text="", icon=""):
		super().__init__(p)
		self.setObjectName("TitleBar")
		self.parent().setWindowFlags(Qt.FramelessWindowHint)
		self.label = QLabel(text, self)
		if icon:
			self.icon = QPushButton(QIcon(abspath(icon)), "", self) if isfile(abspath(icon)) else QPushButton(icons[icon], self)
		else:
			self.icon = QPushButton(QIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)), "", self)
		self.alwaysTop = QPushButton(icons["ti-arrow-circle-up"], self)
		self.minimize = QPushButton(icons["ti-minus"], self)
		self.maximize = QPushButton(icons["ti-angle-up"], self)
		self.closeB = QPushButton(icons["ti-close"], self)

		self.alwaysTop.clicked.connect(self.toggleTopParent)
		self.minimize.clicked.connect(self.minimizeParent)
		self.maximize.clicked.connect(self.maximizeParent)
		self.closeB.clicked.connect(self.closeParent)
		self.alwaysTop.setFocusPolicy(Qt.NoFocus)
		self.minimize.setFocusPolicy(Qt.NoFocus)
		self.maximize.setFocusPolicy(Qt.NoFocus)
		self.closeB.setFocusPolicy(Qt.NoFocus)
		self.icon.setFocusPolicy(Qt.NoFocus)

		self.icon.setObjectName("Icon")
		self.label.setObjectName("Title")
		self.alwaysTop.setObjectName("Button")
		self.minimize.setObjectName("Button")
		self.maximize.setObjectName("Button")
		self.closeB.setObjectName("Button")

		self.parent().onTop = False

		self.setStyleSheet(CustomTitleBar.baseStyleSheet)
		self.resizeEvent()


	def toggleTopParent(self):
		if self.parent().onTop:
			self.parent().setWindowFlags(Qt.FramelessWindowHint)
			self.alwaysTop.setText(icons["ti-arrow-circle-up"])
			self.parent().show()
		else:
			self.parent().setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
			self.alwaysTop.setText(icons["ti-angle-double-up"])
			self.parent().show()
		self.parent().onTop = not self.parent().onTop
	def minimizeParent(self):
		self.parent().setWindowState(Qt.WindowMinimized)
	def maximizeParent(self):
		if self.parent().windowState() != Qt.WindowMaximized:
			self.parent().setWindowState(Qt.WindowMaximized)
		else:
			self.parent().setWindowState(Qt.WindowActive)
	def closeParent(self):
		self.parent().close()

	def setTitle(self, text):
		self.label.setText(text)
	def setIcon(self, icon):
		if isfile(abspath(icon)):
			self.setText("")
			self.icon.setIcon(QIcon(abspath(icon)))
		else:
			self.icon.setIcon(None)
			self.setText(icons[icon])


	def mouseMoveEvent(self, event):
		if event.buttons() & Qt.LeftButton:
			if app.widgetAt(self.m_dragPosition + self.parent().geometry().topLeft()) == self.label:
				if self.parent().windowState() != Qt.WindowMaximized:
					self.parent().move(event.globalPos() - self.m_dragPosition);
					event.accept()
				else:
					self.m_dragPosition = event.globalPos() - self.parent().frameGeometry().topLeft()
					if self.parent().size() == self.parent().maximumSize():
						self.parent().setSize(self.parent().minimumSize())
					self.parent().setWindowState(Qt.WindowActive)
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.m_dragPosition = event.pos()
			event.accept()
	def resizeEvent(self, e=None):
		self.maximize.setText(icons["ti-angle-up"] if self.parent().windowState() != Qt.WindowMaximized else icons["ti-angle-down"])
		self.icon.setGeometry(0, 0, 20, 20)
		self.label.setGeometry(25, 0, self.parent().width()-80, 20)
		self.alwaysTop.setGeometry(self.parent().width()-80, 0, 20, 19)
		self.minimize.setGeometry(self.parent().width()-60, 0, 20, 19)
		self.maximize.setGeometry(self.parent().width()-40, 0, 20, 19)
		self.closeB.setGeometry(self.parent().width()-20, 0, 20, 19)












app = QApplication(argv)
QFontDatabase.addApplicationFont("themify.ttf")

mw = MainWindow()
mw.show()

exit(app.exec_())