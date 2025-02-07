
add_executable(openMVG_main_SfMInit_ImageListingFromKnownPoses
  main_SfMInit_ImageListingFromKnownPoses.cpp
    io_readGTInterface.hpp
    io_readGTStrecha.hpp
    io_readGTMiddleBury.hpp
    io_readGTDTUMVS.hpp
    io_readGTETH3D.hpp
    io_readGTKitti.hpp
    io_readGTARkit.hpp
)
target_link_libraries(openMVG_main_SfMInit_ImageListingFromKnownPoses
  PRIVATE
    openMVG_system
    openMVG_image
    openMVG_features
    openMVG_sfm
    openMVG_exif
    ${STLPLUS_LIBRARY}
)

# Installation rules
set_property(TARGET openMVG_main_SfMInit_ImageListingFromKnownPoses PROPERTY FOLDER OpenMVG/software)
install(TARGETS openMVG_main_SfMInit_ImageListingFromKnownPoses DESTINATION bin/)

SET(OPENMVG_TUTORIAL_IN_FILE "${CMAKE_CURRENT_LIST_DIR}/SfM_StructurePipeline.py.in")
CONFIGURE_FILE(${OPENMVG_TUTORIAL_IN_FILE}
    "${CMAKE_CURRENT_BINARY_DIR}/SfM_StructurePipeline.py" @ONLY)

SET(OPENMVG_TUTORIAL_IN_FILE "${CMAKE_CURRENT_LIST_DIR}/SfM_IncrementalPipeline.py.in")
CONFIGURE_FILE(${OPENMVG_TUTORIAL_IN_FILE}
    "${CMAKE_CURRENT_BINARY_DIR}/SfM_IncrementalPipeline.py" @ONLY)

SET(OPENMVG_TUTORIAL_IN_FILE "${CMAKE_CURRENT_LIST_DIR}/SfM_get_poses_gt.py.in")
CONFIGURE_FILE(${OPENMVG_TUTORIAL_IN_FILE}
    "${CMAKE_CURRENT_BINARY_DIR}/SfM_get_poses_gt.py" @ONLY)

SET(OPENMVG_TUTORIAL_IN_FILE "${CMAKE_CURRENT_LIST_DIR}/SfM_IncrementalPipelineGpsPrior.py.in")
CONFIGURE_FILE(${OPENMVG_TUTORIAL_IN_FILE}
    "${CMAKE_CURRENT_BINARY_DIR}/SfM_IncrementalPipelineGpsPrior.py" @ONLY)

    SET(OPENMVG_TUTORIAL_IN_FILE "${CMAKE_CURRENT_LIST_DIR}/SfM_IncrementalPipeline_ordered.py.in")
    CONFIGURE_FILE(${OPENMVG_TUTORIAL_IN_FILE}
        "${CMAKE_CURRENT_BINARY_DIR}/SfM_IncrementalPipeline_ordered.py" @ONLY)