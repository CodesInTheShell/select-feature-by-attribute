# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectFeatByAttr
                                 A QGIS plugin
 Selecting features by their attirbute
                             -------------------
        begin                : 2017-12-28
        copyright            : (C) 2017 by CodesInTheShell
        email                : dhans053008@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SelectFeatByAttr class from file SelectFeatByAttr.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .select_feat_by_attri import SelectFeatByAttr
    return SelectFeatByAttr(iface)
