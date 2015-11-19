import mari
import PySide
core = PySide.QtCore
gui = PySide.QtGui
w = gui.QWidget()

def symmetryBakeX():

    def bufferBake():
        paint_buffer = mari.canvases.paintBuffer()
        paint_buffer.bake()

    bufferBake()    


    def cameraInversion():

        camera = mari.canvases.current().camera()

        lookAt = camera.lookAt()
        up = camera.up()
        translation = camera.translation()
    
        camera.setTranslation( mari.VectorN(-translation.x(),translation.y(),translation.z()))
        camera.setUp( mari.VectorN(-up.x(),up.y(),up.z()))
        camera.setLookAt( mari.VectorN(-lookAt.x(),lookAt.y(),lookAt.z()))


    cameraInversion()

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()


    

    bufferBake()

    cameraInversion()

    paintBufferFlip((-1,1))

    paintBufferRotate()

    paintBufferTranslation()


actionSymmetryBakeX = mari.actions.create( 'Bake Symmetry X', 'symmetryBakeX()' )

actionSymmetryBakeX.setShortcut("Shift+X")

mari.menus.addAction( actionSymmetryBakeX, "MainWindow/d&eTools/&Symmetry" )






def symmetryBakeY():

    def bufferBake():
        paint_buffer = mari.canvases.paintBuffer()
        paint_buffer.bake()

    bufferBake()    


    def cameraInversion():

        camera = mari.canvases.current().camera()

        lookAt = camera.lookAt()
        up = camera.up()
        translation = camera.translation()
    
        camera.setTranslation( mari.VectorN(translation.x(),-translation.y(),translation.z()))
        camera.setUp( mari.VectorN(up.x(),-up.y(),up.z()))
        camera.setLookAt( mari.VectorN(lookAt.x(),-lookAt.y(),lookAt.z()))


    cameraInversion()

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()


    

    bufferBake()

    cameraInversion()

    paintBufferFlip((-1,1))

    paintBufferRotate()

    paintBufferTranslation()


actionSymmetryBakeY = mari.actions.create( 'Bake Symmetry Y', 'symmetryBakeY()' )

actionSymmetryBakeY.setShortcut("Shift+Y")

mari.menus.addAction( actionSymmetryBakeY, "MainWindow/d&eTools/&Symmetry" )



def symmetryBakeZ():

    def bufferBake():
        paint_buffer = mari.canvases.paintBuffer()
        paint_buffer.bake()

    bufferBake()    


    def cameraInversion():

        camera = mari.canvases.current().camera()

        lookAt = camera.lookAt()
        up = camera.up()
        translation = camera.translation()
    
        camera.setTranslation( mari.VectorN(translation.x(),translation.y(),-translation.z()))
        camera.setUp( mari.VectorN(up.x(),up.y(),-up.z()))
        camera.setLookAt( mari.VectorN(lookAt.x(),lookAt.y(),-lookAt.z()))


    cameraInversion()

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()


    

    bufferBake()

    cameraInversion()

    paintBufferFlip((-1,1))

    paintBufferRotate()

    paintBufferTranslation()


actionSymmetryBakeZ = mari.actions.create( 'Bake Symmetry Z', 'symmetryBakeZ()' )

actionSymmetryBakeZ.setShortcut("Shift+Z")

mari.menus.addAction( actionSymmetryBakeZ, "MainWindow/d&eTools/&Symmetry" )


def cameraInverseX():

    camera = mari.canvases.current().camera()

    lookAt = camera.lookAt()
    up = camera.up()
    translation = camera.translation()


    
    camera.setTranslation( mari.VectorN(-translation.x(),translation.y(),translation.z()))
    camera.setUp( mari.VectorN(-up.x(),up.y(),up.z()))
    camera.setLookAt( mari.VectorN(-lookAt.x(),lookAt.y(),lookAt.z()))

    core = PySide.QtCore

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()



actionCameraInverseX = mari.actions.create( 'Invert Canvas X', 'cameraInverseX()' )

actionCameraInverseX.setShortcut("Ctrl+Shift+X")

mari.menus.addAction( actionCameraInverseX, "MainWindow/d&eTools/&Symmetry" )



def cameraInverseY():

    camera = mari.canvases.current().camera()

    lookAt = camera.lookAt()
    up = camera.up()
    translation = camera.translation()


    
    camera.setTranslation( mari.VectorN(translation.x(),-translation.y(),translation.z()))
    camera.setUp( mari.VectorN(up.x(),-up.y(),up.z()))
    camera.setLookAt( mari.VectorN(lookAt.x(),-lookAt.y(),lookAt.z()))

    core = PySide.QtCore

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()



actionCameraInverseY = mari.actions.create( 'Invert Canvas Y', 'cameraInverseY()' )

actionCameraInverseY.setShortcut("Ctrl+Shift+Y")

mari.menus.addAction( actionCameraInverseY, "MainWindow/d&eTools/&Symmetry" )


def cameraInverseZ():

    camera = mari.canvases.current().camera()

    lookAt = camera.lookAt()
    up = camera.up()
    translation = camera.translation()


    
    camera.setTranslation( mari.VectorN(translation.x(),translation.y(),-translation.z()))
    camera.setUp( mari.VectorN(up.x(),up.y(),-up.z()))
    camera.setLookAt( mari.VectorN(lookAt.x(),lookAt.y(),-lookAt.z()))

    core = PySide.QtCore

    def paintBufferFlip( scaleFactor ):
            paintBuffer = mari.canvases.paintBuffer()
            scale = paintBuffer.scale()
            scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
            paintBuffer.setScale( scale )

    paintBufferFlip((-1,1))

    def paintBufferRotate():
            paint_buffer = mari.canvases.paintBuffer()
            rotation = paint_buffer.rotation()
            paint_buffer.setRotation( 360-rotation )

    paintBufferRotate()


    def paintBufferTranslation():

            paint_buffer = mari.canvases.paintBuffer()
            translation = paint_buffer.translation()
            paint_buffer.setTranslation(core.QPointF(-translation.x(), translation.y()))

    paintBufferTranslation()



actionCameraInverseZ = mari.actions.create( 'Invert Canvas Z', 'cameraInverseZ()' )

actionCameraInverseZ.setShortcut("Ctrl+Shift+Z")

mari.menus.addAction( actionCameraInverseZ, "MainWindow/d&eTools/&Symmetry" )







pal = mari.palettes.create("Symmetry Tools",w)
pal.setBodyWidget(w)
pal.show()
gui = PySide.QtGui
dir(PySide)
layout = gui.QHBoxLayout()
w.setLayout(layout)

pbSymmetryX = gui.QPushButton("Bake X")
layout.addWidget(pbSymmetryX)

pbSymmetryY = gui.QPushButton("Bake Y")
layout.addWidget(pbSymmetryY)

pbSymmetryZ = gui.QPushButton("Bake Z")
layout.addWidget(pbSymmetryZ)

connect(pbSymmetryX.clicked, symmetryBakeX)
connect(pbSymmetryY.clicked, symmetryBakeY)
connect(pbSymmetryZ.clicked, symmetryBakeZ)